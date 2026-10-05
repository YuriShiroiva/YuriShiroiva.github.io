# Portfólio de Yuri Shiroiva

Cientista de dados e engenheiro de IA em Curitiba. LLMs e agentes em produção, séries temporais, machine learning e deep learning com imagens de satélite.

**Site:** https://yurishiroiva.github.io

Site estático (HTML, CSS e JS), sem build. Usa [GSAP](https://gsap.com) com ScrollTrigger para as animações, [Lenis](https://lenis.darkroom.engineering) para o scroll suave, a fonte Inter Tight do Google Fonts e os logos da seção Stack do [Simple Icons](https://simpleicons.org). Tudo vem por CDN.

## Projetos

| Projeto | Página |
|---|---|
| Talhões por satélite (TCC, PUCPR) | [`projetos/talhoes.html`](projetos/talhoes.html) |
| Redes neurais: câmbio e CO₂ | [`projetos/redes-neurais.html`](projetos/redes-neurais.html) |
| FolhaSã: doenças em folhas de tomate | [`projetos/folhasa.html`](projetos/folhasa.html) |
| Detecção de falhas industriais | [`projetos/falhas.html`](projetos/falhas.html) |

## Rodar localmente

```bash
python -m http.server 4321
```

Depois abra http://localhost:4321.

## Estrutura

```
index.html            página inicial (textos, links, cards de projeto)
projetos/*.html       uma página por projeto
404.html              página de erro (usa caminhos absolutos, começando com /)
css/style.css         visual (cores e fontes nas variáveis do topo, em :root)
js/main.js            loader, scroll, animações, cursor, menu
assets/me/            avatar (hero e menu)
assets/projects/      capa e figuras de cada projeto, uma pasta por página
assets/services/      ilustrações da seção "O que eu faço"
assets/og/            imagens de 1200x630 que aparecem ao compartilhar o link
assets/cv/            currículo em PDF (português e inglês)
robots.txt, sitemap.xml
```

## Capas dos projetos

As capas têm 1600x1280. O card da home e a capa da página do projeto cortam partes diferentes da imagem, e o parallax mexe nela. Por isso o conteúdo importante tem que ficar dentro da faixa **x de 150 a 1450 e y de 270 a 1010**.

## Cache do navegador

O CSS e o JS são carregados com um número de versão (`css/style.css?v=20261005a`). Sempre que mudar esses arquivos, troque o `?v=` nas 6 páginas (`index.html`, `404.html` e `projetos/*.html`) para os visitantes receberem a versão nova. Com imagem que muda mantendo o nome, vale o mesmo: as capas usam `?v=2`.

## Publicar no GitHub Pages

1. Crie um repositório **público** chamado `YuriShiroiva.github.io`.
2. Envie esta pasta para ele (branch `main`).
3. Em *Settings → Pages*, escolha *Deploy from a branch* → `main` / `(root)`.

O site fica em https://yurishiroiva.github.io em um ou dois minutos.
