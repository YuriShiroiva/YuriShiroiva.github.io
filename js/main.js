/* =========================================================
   Portfólio — interações e animações
   GSAP + ScrollTrigger + Lenis (via CDN no index.html)
   ========================================================= */
(() => {
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const hasGsap = typeof window.gsap !== 'undefined' && typeof window.ScrollTrigger !== 'undefined';

  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  window.scrollTo(0, 0);

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
    let size = (200 * avail / natural) * 0.995;
    const maxVh = parseFloat(el.dataset.fitMaxVh);
    if (maxVh) size = Math.min(size, innerHeight * maxVh / 100);
    el.style.fontSize = `${size}px`;
  }
  const fitAll = () => $$('[data-fit]').forEach(fit);

  /* ---------- Split inicial (antes de medir) ---------- */
  const nameChars = $$('[data-split-line]').flatMap((el) => splitChars(el));
  const megaChars = $$('[data-split-chars]').flatMap((el) => {
    el.setAttribute('aria-label', el.textContent.replace(/\s+/g, ' ').trim());
    return [...el.children].flatMap((child) => splitChars(child));
  });
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
  const toggle = $('.dock__toggle');
  const panel = $('.dock__panel');
  function setMenu(open) {
    dock.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
    panel.inert = !open;
  }
  toggle.addEventListener('click', () => setMenu(!dock.classList.contains('is-open')));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });
  document.addEventListener('click', (e) => { if (!dock.contains(e.target)) setMenu(false); });

  /* ---------- Links âncora ---------- */
  $$('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href');
      if (id.length < 2) { e.preventDefault(); return; }
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      setMenu(false);
      if (lenis) lenis.scrollTo(target, { duration: 1.6 });
      else target.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
    });
  });

  /* ---------- Copiar e-mail ---------- */
  $$('[data-copy]').forEach((btn) => {
    const original = btn.textContent;
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(btn.dataset.copy);
        btn.textContent = 'Copiado!';
      } catch {
        btn.textContent = btn.dataset.copy;
      }
      setTimeout(() => { btn.textContent = original; }, 1800);
    });
  });

  /* ---------- Relógio e ano ---------- */
  const clock = $('[data-clock]');
  if (clock) {
    const fmt = new Intl.DateTimeFormat('pt-BR', {
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
    if (document.fonts) document.fonts.ready.then(fitAll);
    return;
  }

  ScrollTrigger.addEventListener('refreshInit', fitAll);

  /* ---------- Hero: card de satélite inclina seguindo o mouse ---------- */
  const scan = $('.scan');
  if (scan && finePointer && !reduceMotion) {
    const intro = $('.intro');
    const rotX = gsap.quickTo(scan, 'rotationX', { duration: 0.9, ease: 'power3' });
    const rotY = gsap.quickTo(scan, 'rotationY', { duration: 0.9, ease: 'power3' });
    const glows = $$('.intro__glow').map((g, i) => ({
      x: gsap.quickTo(g, 'x', { duration: 1.4, ease: 'power3' }),
      y: gsap.quickTo(g, 'y', { duration: 1.4, ease: 'power3' }),
      k: 30 + i * 25,
    }));
    intro.addEventListener('pointermove', (e) => {
      const r = intro.getBoundingClientRect();
      const nx = (e.clientX - r.left) / r.width - 0.5;
      const ny = (e.clientY - r.top) / r.height - 0.5;
      rotY(nx * 24);
      rotX(-ny * 18);
      glows.forEach((g) => { g.x(nx * g.k); g.y(ny * g.k); });
    });
    intro.addEventListener('pointerleave', () => { rotX(0); rotY(0); });
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

    // Hero: textos sobem mais rápido que o card de satélite ao rolar
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
          scrollTrigger: { trigger: next, start: 'top 75%', end: 'top 25%', scrub: true },
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

    // TRABALHOS '26
    reveal(megaChars, {
      yPercent: 110,
      duration: 1.2,
      ease: 'expo.out',
      stagger: 0.035,
      scrollTrigger: { trigger: '.mega', start: 'top 85%' },
    });

    // Cards de projeto
    gsap.utils.toArray('.project').forEach((p, i) => {
      gsap.from(p, {
        y: 90,
        opacity: 0,
        duration: 1.3,
        ease: 'expo.out',
        delay: (i % 2) * 0.1,
        scrollTrigger: { trigger: p, start: 'top 92%' },
      });
    });

    // STACK MODERNA
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
  function intro() {
    const loader = $('.loader');
    const count = $('.loader__count');
    const done = () => {
      document.body.classList.remove('is-loading');
      lenis?.start();
      // chegou com #ancora (ex.: vindo de uma página de projeto)
      const target = location.hash.length > 1 && $(location.hash);
      if (target) {
        if (lenis) lenis.scrollTo(target, { immediate: true, force: true });
        else target.scrollIntoView();
      }
    };

    if (!loader || reduceMotion) {
      loader?.remove();
      (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => {
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
    gsap.set('.scan', { scale: 0.82, opacity: 0 });
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
    const fonts = document.fonts ? document.fonts.ready : Promise.resolve();

    Promise.all([Promise.race([Promise.all([loaded, fonts]), timeout]), counting]).then(() => {
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
        .to('.scan', { scale: 1, opacity: 1, duration: 1.4, ease: 'expo.out' }, '<.1')
        .to(introBits, { y: 0, opacity: 1, duration: 1, ease: 'expo.out', stagger: 0.06 }, '<.2')
        .to(['.topbar', '.topbar__cta'], { autoAlpha: 1, duration: 0.8 }, '<')
        .fromTo('.dock', { autoAlpha: 0, y: 40 }, { autoAlpha: 1, y: 0, duration: 1, ease: 'expo.out' }, '<.1');
    });
  }

  intro();
})();
