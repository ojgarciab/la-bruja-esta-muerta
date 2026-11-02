// Menú móvil, sección actual en la navegación, apariciones al hacer scroll,
// frase que se ilumina palabra a palabra y botones para copiar las órdenes.
(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Menú móvil: panel a pantalla completa
  const toggle = document.querySelector(".menu-toggle");
  const panel = document.getElementById("panel");
  const setMenu = (open) => {
    document.body.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Cerrar el menú" : "Abrir el menú");
    document.body.style.overflow = open ? "hidden" : "";
  };
  toggle.addEventListener("click", () => setMenu(!document.body.classList.contains("menu-open")));
  panel.addEventListener("click", (e) => { if (e.target.closest("a")) setMenu(false); });
  addEventListener("keydown", (e) => { if (e.key === "Escape") setMenu(false); });

  // Sección actual en la navegación
  const links = [...document.querySelectorAll(".nav-links a, .panel a[href^='#']")];
  const sections = [...new Set(links.map((a) => a.getAttribute("href")))]
    .map((h) => document.querySelector(h)).filter(Boolean);
  const current = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (!en.isIntersecting) return;
      const id = "#" + en.target.id;
      links.forEach((a) => {
        if (a.getAttribute("href") === id && !a.classList.contains("btn")) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });
    });
  }, { rootMargin: "-45% 0px -50% 0px" });
  sections.forEach((s) => current.observe(s));

  // Apariciones: una sola vez por elemento
  const reveal = new IntersectionObserver((entries) => {
    entries.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add("in"); reveal.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll(".reveal").forEach((el) => reveal.observe(el));

  // Frase destacada: cada palabra se ilumina al cruzar la línea de activación
  document.querySelectorAll("[data-reveal-words]").forEach((p) => {
    const wrapWords = (node, hl) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === Node.TEXT_NODE) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.append(part); return; }
            const s = document.createElement("span");
            s.className = hl ? "w hl" : "w";
            s.textContent = part;
            frag.append(s);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === Node.ELEMENT_NODE && n.tagName !== "BR") {
          wrapWords(n, hl || n.classList.contains("hl"));
        }
      });
    };
    wrapWords(p, false);
    const words = [...p.querySelectorAll(".w")];
    if (reduce) { words.forEach((w) => w.classList.add("on")); return; }
    let ticking = false;
    const update = () => {
      ticking = false;
      const line = innerHeight * 0.62;
      words.forEach((w) => w.classList.toggle("on", w.getBoundingClientRect().top < line));
    };
    addEventListener("scroll", () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    update();
  });

  // Copiar las órdenes de los bloques de código
  document.querySelectorAll(".code").forEach((box) => {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "copy caption-3";
    btn.innerHTML = '<i class="ph ph-copy" aria-hidden="true"></i><span>Copiar</span>';
    btn.addEventListener("click", async () => {
      const label = btn.querySelector("span");
      try {
        await navigator.clipboard.writeText(box.querySelector("code").innerText);
        label.textContent = "Copiado";
      } catch {
        label.textContent = "Selecciona y copia";
      }
      setTimeout(() => { label.textContent = "Copiar"; }, 2000);
    });
    box.append(btn);
  });
})();
