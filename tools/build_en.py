"""Gera a versão em inglês do site (pasta en/) a partir das páginas em português.

Uso:  python tools/build_en.py
Rode de novo sempre que mudar uma página em português. Se aparecer texto novo sem tradução,
o script lista os trechos e não grava nada: é só acrescentar a tradução em tools/en_strings.py.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from en_strings import KEEP, TR  # noqa: E402

SITE = "https://yurishiroiva.github.io/"
SLUGS = {"talhoes": "field-boundaries", "redes-neurais": "neural-networks", "folhasa": "folhasa", "falhas": "defect-detection"}
IDS = {"inicio": "home", "sobre": "about", "experiencia": "experience", "projetos": "projects", "servicos": "services",
       "contato": "contact", "topo": "top", "plataforma": "platform"}
# página PT -> (página EN, imagem de compartilhamento em inglês)
PAGES = {"index.html": ("en/index.html", "home-en.jpg")}
PAGES.update({f"projetos/{pt}.html": (f"en/projects/{en}.html", f"{pt}-en.jpg" if pt != "folhasa" else "folhasa.jpg")
              for pt, en in SLUGS.items()})

# ajustes de HTML que não são só tradução de texto
RAW = {
    "index.html": [
        # currículo em inglês no botão do topo e no bloco do rodapé
        ('href="assets/cv/Yuri_Shiroiva_Curriculo.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Curriculo.pdf">Currículo <span',
         'href="assets/cv/Yuri_Shiroiva_Resume.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Resume.pdf">Currículo <span'),
        ('href="assets/cv/Yuri_Shiroiva_Curriculo.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Curriculo.pdf"><span class="tile__arrow"',
         'href="assets/cv/Yuri_Shiroiva_Resume.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Resume.pdf"><span class="tile__arrow"'),
        # no contato, o currículo em inglês vem primeiro
        ('          <a class="pill pill--ghost" href="assets/cv/Yuri_Shiroiva_Curriculo.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Curriculo.pdf">Currículo (PT) ↓</a>\n'
         '          <a class="pill pill--ghost" href="assets/cv/Yuri_Shiroiva_Resume.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Resume.pdf">Resume (EN) ↓</a>\n',
         '          <a class="pill pill--ghost" href="assets/cv/Yuri_Shiroiva_Resume.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Resume.pdf">Resume (EN) ↓</a>\n'
         '          <a class="pill pill--ghost" href="assets/cv/Yuri_Shiroiva_Curriculo.pdf?v=3" download="Yuri_Shiroiva_Berbereia_Curriculo.pdf">Currículo (PT) ↓</a>\n'),
        # "Stack moderna" vira "Modern stack": troca a ordem das linhas
        ('<span class="stack__line" data-roll>Stack</span>\n        <span class="stack__line" data-roll>Moderna</span>',
         '<span class="stack__line" data-roll>Moderna</span>\n        <span class="stack__line" data-roll>Stack</span>'),
        ('"jobTitle": "Cientista de Dados e Engenheiro de IA"', '"jobTitle": "Data Scientist and AI Engineer"'),
        ('"url": "https://yurishiroiva.github.io/",', '"url": "https://yurishiroiva.github.io/en/",'),
    ],
}

TEXT = re.compile(r">([^<>]+)<")
ATTR = re.compile(r'\b(alt|title|aria-label|data-cursor|data-text)="([^"]*)"')
META = re.compile(r'(<meta (?:name="description"|property="og:(?:title|description)") content=")([^"]*)(")')
SKIP = re.compile(r"<(script|style|svg)\b.*?</\1>|<!--.*?-->", re.S)
WORD = re.compile(r"[A-Za-zÀ-ÿ]")
NUMBER = re.compile(r"^[\s\d.,%+−\-×]+$")


def translate_segments(html, missing):
    clean = SKIP.sub(lambda m: " " * len(m.group(0)), html)
    spans = [(m.start(1), m.end(1)) for m in TEXT.finditer(clean)]
    spans += [(m.start(2), m.end(2)) for m in ATTR.finditer(clean)]
    spans += [(m.start(2), m.end(2)) for m in META.finditer(html)]
    out, pos = [], 0
    for s, e in sorted(spans):
        raw = html[s:e]
        key = " ".join(raw.split())
        new = raw
        if clean[s:e] != raw:
            pass                                         # contém script, svg ou comentário: não é texto
        elif key and WORD.search(key):
            if key in TR:
                lead = raw[: len(raw) - len(raw.lstrip())]
                trail = raw[len(raw.rstrip()):]
                new = lead + TR[key] + trail
            elif key not in KEEP:
                missing.add(key)
        elif NUMBER.match(raw) and "," in raw:
            new = re.sub(r"(\d),(\d)", r"\1.\2", raw)   # 0,87 -> 0.87
        out.append(html[pos:s]); out.append(new); pos = e
    out.append(html[pos:])
    return "".join(out)


def rewrite_paths(html, page):
    is_index = page == "index.html"

    def fix(m):
        attr, path = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:|^#|^/", path) or not path:
            return m.group(0)
        base, _, frag = path.partition("#")
        if is_index:
            if base.startswith("projetos/"):
                slug = base[len("projetos/"):-len(".html")]
                base = f"projects/{SLUGS[slug]}.html"
            else:
                base = "../" + base                      # assets/, css/, js/
        else:
            if base.startswith("../index.html"):
                pass                                     # en/index.html fica um nível acima, igual
            elif base.startswith("../"):
                base = "../" + base                      # ../assets -> ../../assets
            elif base[:-len(".html")] in SLUGS:
                base = SLUGS[base[:-len(".html")]] + ".html"
        # imagem com versão em inglês (nome-en.webp) quando existir
        m2 = re.match(r"^((?:\.\./)+assets/projects/[^?]+?)\.webp(\?v=\d+)?$", base)
        if m2:
            en_rel = m2.group(1).split("assets/", 1)[1] + "-en.webp"
            if os.path.exists(os.path.join(ROOT, "assets", en_rel)):
                base = m2.group(1) + "-en.webp"
        return f'{attr}="{base}' + (f"#{frag}" if frag else "") + '"'

    return re.sub(r'\b(src|href)="([^"]*)"', fix, html)


def rewrite_ids(html):
    html = re.sub(r'\bid="([^"]+)"', lambda m: f'id="{IDS.get(m.group(1), m.group(1))}"', html)
    return re.sub(r'(href="[^"#]*#)([^"]+)"', lambda m: f'{m.group(1)}{IDS.get(m.group(2), m.group(2))}"', html)


def lang_switch(html, pt_href):
    def repl(m):
        cls = re.search(r'class="(lang[^"]*)"', m.group(0)).group(1)
        return (f'<!-- lang --><nav class="{cls}" aria-label="Language"><a href="{pt_href}" hreflang="pt-BR" lang="pt-BR">PT</a>'
                f'<span aria-hidden="true">/</span><span aria-current="true">EN</span></nav><!-- /lang -->')
    html, n = re.subn(r"<!-- lang -->.*?<!-- /lang -->", repl, html, flags=re.S)
    assert n == 2, f"esperava 2 seletores de idioma, achei {n}"
    return html


def build(page, missing):
    en_path, og_en = PAGES[page]
    s = io.open(os.path.join(ROOT, page), encoding="utf-8").read()
    for old, new in RAW.get(page, []):
        assert s.count(old) == 1, f"{page}: trecho não encontrado: {old[:70]}"
        s = s.replace(old, new)
    s = s.replace('<html lang="pt-BR">', '<html lang="en">', 1)
    pt_url = SITE + ("" if page == "index.html" else page)
    en_url = SITE + ("en/" if page == "index.html" else en_path)
    s = s.replace(f'<link rel="canonical" href="{pt_url}">', f'<link rel="canonical" href="{en_url}">')
    s = s.replace(f'<meta property="og:url" content="{pt_url}">', f'<meta property="og:url" content="{en_url}">')
    s = s.replace('<meta property="og:locale" content="pt_BR">', '<meta property="og:locale" content="en_US">')
    s = re.sub(r'(<meta property="og:image" content="https://yurishiroiva\.github\.io/assets/og/)[^"]+"', rf'\g<1>{og_en}"', s)
    s = rewrite_paths(s, page)
    s = rewrite_ids(s)
    s = translate_segments(s, missing)
    pt_href = "../" if page == "index.html" else f"../../{page}"
    s = lang_switch(s, pt_href)
    return en_path, s


def main():
    missing, outputs = set(), []
    for page in PAGES:
        outputs.append(build(page, missing))
    if missing:
        print("Trechos sem tradução (acrescente em tools/en_strings.py):")
        for m in sorted(missing):
            print("  -", m)
        sys.exit(1)
    for path, html in outputs:
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        io.open(full, "w", encoding="utf-8", newline="\n").write(html)
        print("ok", path)


if __name__ == "__main__":
    main()
