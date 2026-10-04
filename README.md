# Portfólio — Yuri Shiroiva

Desenvolvedor Python e de IA aplicada: visão computacional, deep learning com imagens de satélite e APIs em produção.

**Site:** https://yurishiroiva.github.io

Site estático (HTML + CSS + JS), sem build. Animações com [GSAP](https://gsap.com) + ScrollTrigger e scroll suave com [Lenis](https://lenis.darkroom.engineering), ambos via CDN.

## Projetos

| Projeto | Página |
|---|---|
| Talhões por satélite (TCC, PUCPR) | [`projetos/talhoes.html`](projetos/talhoes.html) |
| Plataforma de talhões | [`projetos/talhoes.html#plataforma`](projetos/talhoes.html) |
| FolhaSã — doenças em folhas de tomate | [`projetos/folhasa.html`](projetos/folhasa.html) |
| Detecção de falhas industriais | [`projetos/falhas.html`](projetos/falhas.html) |

## Rodar localmente

```bash
python -m http.server 4321
```

Depois abra http://localhost:4321.

## Estrutura

```
index.html          → página inicial (textos, links, cards de projeto)
projetos/*.html     → uma página por projeto
css/style.css       → visual (cores e fontes nas variáveis do topo, em :root)
js/main.js          → loader, scroll, animações, cursor, menu
assets/             → imagens (capas e figuras dos projetos)
```

## O que ainda falta preencher

| Onde | O quê |
|---|---|
| `index.html` e `projetos/*.html` | Links do LinkedIn e Instagram |
| `assets/me.svg` | Sua foto (pode ser `.jpg`; atualize o `src` em `#sobre`) |

## Publicar no GitHub Pages

1. Crie um repositório **público** chamado `YuriShiroiva.github.io`.
2. Envie esta pasta para ele (branch `main`).
3. Em *Settings → Pages*, escolha *Deploy from a branch* → `main` / `(root)`.

O site fica em https://yurishiroiva.github.io em um ou dois minutos.
