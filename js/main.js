/* =========================================================
   Portfólio: interações e animações
   GSAP + ScrollTrigger + Lenis (via CDN, no fim de cada página)
   ========================================================= */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';
  const isEn = document.documentElement.lang.startsWith('en');
  const t = (pt, en) => (isEn ? en : pt);

  // voltando pelo "Voltar" do navegador: sem loader e na mesma altura de antes
  const returning = performance.getEntriesByType?.('navigation')[0]?.type === 'back_forward';
  const scrollKey = `scroll:${location.pathname}`;
  addEventListener('pagehide', () => {
    try { sessionStorage.setItem(scrollKey, String(Math.round(scrollY))); } catch {}
  });
  const savedScroll = () => {
    try { return Number(sessionStorage.getItem(scrollKey)) || 0; } catch { return 0; }
  };

  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  window.scrollTo(0, 0);

  // espera a fonte, mas no máximo 1,5 s (rede lenta não pode travar a página)
  const fontsReady = () => Promise.race([
    document.fonts ? document.fonts.ready : Promise.resolve(),
    new Promise((res) => setTimeout(res, 1500)),
  ]);

  /* ---------- Split de texto ---------- */
  function splitChars(el, { roll = false } = {}) {
    const text = el.textContent.trim();
    el.textContent = '';
    const inners = [];
    [...text].forEach((ch, i) => {
      const outer = document.createElement('span');
      outer.className = 'c';
      outer.setAttribute('aria-hidden', 'true');
      if (ch === ' ') {
        outer.innerHTML = '&nbsp;';
        el.append(outer);
        return;
      }
      const inner = document.createElement('span');
      inner.className = roll ? 'c__in roll-pair' : 'c__in';
      inner.style.setProperty('--ci', i);
      if (roll) inner.innerHTML = `<span>${ch}</span><span>${ch}</span>`;
      else inner.textContent = ch;
      outer.append(inner);
      el.append(outer);
      inners.push(inner);
    });
    return inners;
  }

  function splitWords(el, masked) {
    const out = [];
    const nodes = [...el.childNodes];
    el.textContent = '';
    nodes.forEach((node) => {
      if (node.nodeType !== Node.TEXT_NODE) {
        el.append(node);
        return;
      }
      node.textContent.split(/(\s+)/).forEach((part) => {
        if (!part) return;
        if (!part.trim()) {
          el.append(' ');
          return;
        }
        const w = document.createElement('span');
        if (masked) {
          w.className = 'w';
          const inner = document.createElement('span');
          inner.className = 'w__in';
          inner.textContent = part;
          w.append(inner);
          out.push(inner);
        } else {
          w.textContent = part;
          out.push(w);
        }
        el.append(w);
      });
    });
    return out;
  }

  /* ---------- Texto que ocupa a largura toda ---------- */
  function fit(el) {
    const cs = getComputedStyle(el);
    const padX = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight);
    // mede em px de layout (offsetWidth ignora transforms das animações)
    el.style.fontSize = '200px';
    const avail = el.clientWidth - padX;
    el.style.width = 'max-content';
    const natural = el.offsetWidth - padX;
    el.style.width = '';
    if (!avail || !natural) return;
    el.style.fontSize = `${(200 * avail / natural) * 0.995}px`;
  }
  const fitAll = () => $$('[data-fit]').forEach(fit);

  /* ---------- Split inicial (antes de medir) ---------- */
  const nameChars = $$('[data-split-line]').flatMap((el) => splitChars(el));
  const rollChars = $$('[data-roll]').flatMap((el) => splitChars(el, { roll: true }));
  fitAll();

  /* ---------- Smooth scroll ---------- */
  let lenis = null;
  if (hasGsap) gsap.registerPlugin(ScrollTrigger);
  if (!reduceMotion && window.Lenis) {
    lenis = new Lenis({ lerp: 0.1 });
    if (hasGsap) {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    } else {
      const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); };
      requestAnimationFrame(raf);
    }
    lenis.stop();
  }

  /* ---------- Dock / menu ---------- */
  const dock = $('.dock');
  const dockToggle = $('.dock__toggle');
  const dockPanel = $('.dock__panel');
  function setMenu(open) {
    // o foco sai do menu antes de ele ficar inerte (senão vai parar no <body>)
    if (!open && dockPanel.contains(document.activeElement)) dockToggle.focus();
    dock.classList.toggle('is-open', open);
    dockToggle.setAttribute('aria-expanded', String(open));
    dockToggle.setAttribute('aria-label', open ? t('Fechar menu', 'Close menu') : t('Abrir menu', 'Open menu'));
    dockPanel.inert = !open;
  }
  dockToggle.addEventListener('click', (e) => {
    const open = !dock.classList.contains('is-open');
    setMenu(open);
    // aberto pelo teclado (Enter/Espaço): o foco vai para o primeiro link
    if (open && e.detail === 0) $('a', dockPanel)?.focus();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
  document.addEventListener('click', (e) => { if (!dock.contains(e.target)) setMenu(false); });

  /* ---------- Experiência: caixas que abrem ao clicar ---------- */
  $$('.job__head').forEach((btn) => {
    const job = btn.closest('.job');
    const jobPanel = document.getElementById(btn.getAttribute('aria-controls'));
    btn.addEventListener('click', () => {
      const open = !job.classList.contains('is-open');
      job.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
      jobPanel.inert = !open;
    });
    // a altura da página muda: recalcula as animações de scroll abaixo
    jobPanel.addEventListener('transitionend', (e) => {
      if (e.propertyName === 'grid-template-rows' && hasGsap) ScrollTrigger.refresh();
    });
  });

  /* ---------- Links âncora ---------- */
  const byHash = (hash) => (hash.length > 1 ? document.getElementById(decodeURIComponent(hash.slice(1))) : null);
  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) { e.preventDefault(); return; }
      const target = byHash(id);
      if (!target) return;
      e.preventDefault();
      setMenu(false);
      if (lenis) lenis.scrollTo(target, { duration: 1.6 });
      else target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
      // leva o foco junto (teclado e leitor de tela continuam dali)
      if (!target.hasAttribute('tabindex')) target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });
  });

  /* ---------- Relógio e ano ---------- */
  const clock = $('[data-clock]');
  if (clock) {
    const fmt = new Intl.DateTimeFormat(t('pt-BR', 'en-GB'), {
      timeZone: 'America/Sao_Paulo', hour: '2-digit', minute: '2-digit', second: '2-digit',
    });
    const tick = () => { clock.textContent = fmt.format(new Date()); };
    tick();
    setInterval(tick, 1000);
  }
  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Logos: fallback se o ícone não carregar ---------- */
  $$('.logo img').forEach((img) => {
    const swap = () => {
      const b = document.createElement('b');
      b.className = 'logo__fallback';
      b.textContent = img.nextElementSibling.textContent.slice(0, 2);
      img.replaceWith(b);
    };
    if (img.complete && img.naturalWidth === 0) swap();
    else img.addEventListener('error', swap, { once: true });
  });

  /* ---------- Sem GSAP: só mostra o site ---------- */
  if (!hasGsap) {
    $('.loader')?.remove();
    document.body.classList.remove('is-loading');
    lenis?.start();
    addEventListener('resize', fitAll);
    fontsReady().then(fitAll);
    return;
  }

  ScrollTrigger.addEventListener('refreshInit', fitAll);

  /* ---------- Hero: avatar acompanha o mouse ---------- */
  const avatar = $('.avatar');
  if (avatar && finePointer && !reduceMotion) {
    const hero = $('.intro');
    const rotX = gsap.quickTo(avatar, 'rotationX', { duration: 0.9, ease: 'power3' });
    const rotY = gsap.quickTo(avatar, 'rotationY', { duration: 0.9, ease: 'power3' });
    const glows = $$('.intro__glow').map((g, i) => ({
      x: gsap.quickTo(g, 'x', { duration: 1.4, ease: 'power3' }),
      y: gsap.quickTo(g, 'y', { duration: 1.4, ease: 'power3' }),
      k: 30 + i * 25,
    }));
    hero.addEventListener('pointermove', (e) => {
      const r = hero.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      rotY(nx * 10);
      rotX(-ny * 6);
      glows.forEach((g) => { g.x(nx * g.k); g.y(ny * g.k); });
    });
    hero.addEventListener('pointerleave', () => { rotX(0); rotY(0); });
  }

  /* ---------- Cursor ---------- */
  if (finePointer) {
    const cursor = $('.cursor');
    const label = $('.cursor__label');
    const xTo = gsap.quickTo(cursor, 'x', { duration: 0.45, ease: 'power3' });
    const yTo = gsap.quickTo(cursor, 'y', { duration: 0.45, ease: 'power3' });
    addEventListener('pointermove', (e) => {
      cursor.classList.add('is-visible');
      xTo(e.clientX);
      yTo(e.clientY);
    });
    document.documentElement.addEventListener('mouseleave', () => cursor.classList.remove('is-visible'));
    $$('[data-cursor]').forEach((el) => {
      el.addEventListener('pointerenter', () => {
        label.textContent = el.dataset.cursor;
        cursor.classList.add('is-label');
      });
      el.addEventListener('pointerleave', () => cursor.classList.remove('is-label'));
    });
    $$('a:not([data-cursor]), button:not([data-cursor])').forEach((el) => {
      el.addEventListener('pointerenter', () => cursor.classList.add('is-hover'));
      el.addEventListener('pointerleave', () => cursor.classList.remove('is-hover'));
    });
  }

  /* ---------- Botões magnéticos ---------- */
  if (finePointer && !reduceMotion) {
    $$('.magnetic').forEach((el) => {
      const xTo = gsap.quickTo(el, 'x', { duration: 0.8, ease: 'elastic.out(1, .4)' });
      const yTo = gsap.quickTo(el, 'y', { duration: 0.8, ease: 'elastic.out(1, .4)' });
      el.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        xTo((e.clientX - r.left - r.width / 2) * 0.3);
        yTo((e.clientY - r.top - r.height / 2) * 0.35);
      });
      el.addEventListener('pointerleave', () => { xTo(0); yTo(0); });
    });
  }

  /* ---------- Animações de scroll ---------- */
  // anima só se os alvos existirem na página atual (home ou página de projeto)
  const reveal = (targets, vars) => {
    const list = gsap.utils.toArray(targets);
    if (list.length) gsap.from(list, vars);
  };

  function initScroll() {
    const mm = gsap.matchMedia();

    // Hero: textos sobem e somem mais rápido que o avatar ao rolar
    mm.add('(prefers-reduced-motion: no-preference)', () => {
      if (!$('.intro')) return;
      const st = () => ({ trigger: '.intro', start: 'top top', end: 'bottom top', scrub: true });
      gsap.to('.intro__left, .intro__right', { yPercent: -30, opacity: 0.15, ease: 'none', scrollTrigger: st() });
      gsap.to('.intro__visual', { yPercent: 14, scale: 0.88, ease: 'none', scrollTrigger: st() });
    });

    // Serviços: cards empilhados que encolhem quando o próximo chega
    mm.add('(min-width: 768px) and (prefers-reduced-motion: no-preference)', () => {
      const cards = gsap.utils.toArray('.service');
      cards.forEach((card, i) => {
        const next = cards[i + 1];
        if (!next) return;
        gsap.to(card, {
          scale: 0.94,
          filter: 'brightness(.5)',
          ease: 'none',
          scrollTrigger: { trigger: next, start: 'top 38%', end: 'top 16%', scrub: true },
        });
      });
    });

    if (reduceMotion) return;

    // Títulos em linhas
    $$('[data-reveal="lines"]').forEach((el) => {
      const words = splitWords(el, true);
      gsap.from(words, {
        yPercent: 110,
        duration: 1.1,
        ease: 'expo.out',
        stagger: 0.012,
        scrollTrigger: { trigger: el, start: 'top 85%' },
      });
    });

    // Fade simples
    $$('[data-reveal="fade"]').forEach((el) => {
      gsap.from(el, {
        y: 60,
        opacity: 0,
        duration: 1.2,
        ease: 'expo.out',
        scrollTrigger: { trigger: el, start: 'top 88%' },
      });
    });

    // Parágrafo que "acende" palavra por palavra
    $$('[data-scrub-words]').forEach((el) => {
      const words = splitWords(el, false);
      gsap.fromTo(words, { opacity: 0.14 }, {
        opacity: 1,
        ease: 'none',
        stagger: 0.1,
        scrollTrigger: { trigger: el, start: 'top 80%', end: 'bottom 50%', scrub: true },
      });
    });

    // Parallax nas imagens
    $$('[data-parallax]').forEach((img) => {
      gsap.fromTo(img, { yPercent: -6 }, {
        yPercent: 6,
        ease: 'none',
        scrollTrigger: { trigger: img.parentElement, start: 'top bottom', end: 'bottom top', scrub: true },
      });
    });

    // Título "Stack moderna"
    reveal(rollChars, {
      yPercent: 50,
      duration: 1.3,
      ease: 'expo.out',
      stagger: 0.035,
      scrollTrigger: { trigger: '.stack__title', start: 'top 80%' },
    });

    reveal('.logo', {
      opacity: 0,
      y: 30,
      duration: 0.9,
      ease: 'expo.out',
      stagger: 0.04,
      scrollTrigger: { trigger: '.logos', start: 'top 88%' },
    });

    // Medidores (página de projeto)
    $$('.meter__fill').forEach((el) => {
      gsap.from(el, {
        scaleX: 0,
        duration: 1.4,
        ease: 'expo.out',
        scrollTrigger: { trigger: el, start: 'top 90%' },
      });
    });

    // Rodapé
    reveal('.tile', {
      opacity: 0,
      y: 40,
      duration: 1,
      ease: 'expo.out',
      stagger: 0.06,
      scrollTrigger: { trigger: '.bento', start: 'top 90%' },
    });
    if ($('.bento__name span')) gsap.fromTo('.bento__name span', { filter: 'blur(28px)', opacity: 0.15, scale: 0.92 }, {
      filter: 'blur(0px)',
      opacity: 1,
      scale: 1,
      ease: 'none',
      scrollTrigger: { trigger: '.bento', start: 'top 85%', end: 'bottom bottom', scrub: true },
    });
  }

  /* ---------- Loader + entrada do hero ---------- */
  function playIntro() {
    const loader = $('.loader');
    const count = $('.loader__count');
    const done = () => {
      document.body.classList.remove('is-loading');
      lenis?.start();
      // chegou com #ancora (ex.: vindo de uma página de projeto) ou voltando pelo navegador
      const target = byHash(location.hash);
      const y = returning && !target ? savedScroll() : 0;
      if (target) {
        if (lenis) lenis.scrollTo(target, { immediate: true, force: true });
        else target.scrollIntoView();
      } else if (y) {
        if (lenis) lenis.scrollTo(y, { immediate: true, force: true });
        else window.scrollTo(0, y);
      }
    };

    if (!loader || reduceMotion || returning) {
      loader?.remove();
      fontsReady().then(() => {
        fitAll();
        initScroll();
        ScrollTrigger.refresh();
        done();
      });
      return;
    }

    const introBits = '.intro__hello, .intro__actions, .intro__label, .intro__role, .intro__summary, .intro__social, .intro__hint';
    gsap.set(nameChars, { yPercent: 115 });
    gsap.set(introBits, { y: 30, opacity: 0 });
    gsap.set('.avatar', { yPercent: 12, opacity: 0 });
    gsap.set('.intro__bg', { opacity: 0 });
    gsap.set(['.topbar', '.topbar__cta', '.dock'], { autoAlpha: 0 });
    gsap.set(loader, { clipPath: 'inset(0% 0% 0% 0%)' });

    const counter = { v: 0 };
    const counting = gsap.to(counter, {
      v: 100,
      duration: 1.1,
      ease: 'power3.inOut',
      onUpdate: () => { count.textContent = Math.round(counter.v); },
    });
    const loaded = new Promise((res) => {
      if (document.readyState === 'complete') res();
      else addEventListener('load', res, { once: true });
    });
    const timeout = new Promise((res) => setTimeout(res, 4000));

    Promise.all([Promise.race([Promise.all([loaded, fontsReady()]), timeout]), counting]).then(() => {
      fitAll();
      initScroll();
      ScrollTrigger.refresh();

      gsap.timeline({
        onComplete: () => loader.remove(),
      })
        .to(count, { yPercent: -100, opacity: 0, duration: 0.45, ease: 'power2.in' })
        .to(loader, { clipPath: 'inset(0% 0% 100% 0%)', duration: 1.1, ease: 'expo.inOut' }, '-=.1')
        .add(done, '-=.5')
        .to('.intro__bg', { opacity: 1, duration: 1.4, ease: 'power2.out' }, '-=.6')
        .to(nameChars, { yPercent: 0, duration: 1.2, ease: 'expo.out', stagger: 0.03 }, '<')
        .to('.avatar', { yPercent: 0, opacity: 1, duration: 1.4, ease: 'expo.out' }, '<.1')
        .to(introBits, { y: 0, opacity: 1, duration: 1, ease: 'expo.out', stagger: 0.06 }, '<.2')
        .to(['.topbar', '.topbar__cta'], { autoAlpha: 1, duration: 0.8 }, '<')
        .fromTo('.dock', { autoAlpha: 0, y: 40 }, { autoAlpha: 1, y: 0, duration: 1, ease: 'expo.out' }, '<.1');
    });
  }

  playIntro();
})();
