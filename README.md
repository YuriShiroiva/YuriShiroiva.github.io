# Portfólio — Yuri Shiroiva

Desenvolvedor Python e de IA aplicada: visão computacional, deep learning com imagens de satélite e APIs em produção.

**Site:** https://yurishiroiva.github.io

Site estático (HTML + CSS + JS), sem build. Animações com [GSAP](https://gsap.com) + ScrollTrigger e scroll suave com [Lenis](https://lenis.darkroom.engineering), ambos via CDN.

## Projetos

| Projeto | Página |
|---|---|
| Talhões por satélite (TCC, PUCPR) | [`projetos/talhoes.html`](projetos/talhoes.html) |
| Redes neurais: câmbio e CO₂ | [`projetos/redes-neurais.html`](projetos/redes-neurais.html) |
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

- Link do LinkedIn (hero, rodapé e dock).
- Currículo em PDF (botão no hero).

## Créditos

O hero foi inspirado no portfólio de [Moncy Yohannan](https://github.com/MoncyDev/Portfolio-Website): a implementação é própria e não usa código nem assets 3D do original.

## Cache do navegador

O CSS e o JS são carregados com um número de versão (`css/style.css?v=20261004k`). Sempre que mudar esses arquivos, troque o `?v=` nas 4 páginas (`index.html` e `projetos/*.html`) para os visitantes receberem a versão nova.

## Publicar no GitHub Pages

1. Crie um repositório **público** chamado `YuriShiroiva.github.io`.
2. Envie esta pasta para ele (branch `main`).
3. Em *Settings → Pages*, escolha *Deploy from a branch* → `main` / `(root)`.

O site fica em https://yurishiroiva.github.io em um ou dois minutos.
