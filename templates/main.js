// Al hacer clic en una tarjeta, se marca como activa y se actualiza la sección "Selección".
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    const p = window.PERSONAJES.find(x => x.id === Number(card.dataset.id));
    if (!p) return;

    document.querySelectorAll('.card').forEach(c => {
      c.classList.remove('is-active');
      c.setAttribute('aria-pressed', 'false');
    });
    card.classList.add('is-active');
    card.setAttribute('aria-pressed', 'true');

    const img = document.getElementById('sel-img');
    img.style.visibility = 'visible';
    img.src = window.IMG_BASE + p.img;
    img.alt = p.nombre;

    document.getElementById('sel-name').textContent = p.nombre;
    document.getElementById('sel-desc').textContent = p.descripcion;
    document.getElementById('sel-arma').textContent = p.arma;
    document.getElementById('sel-arma-desc').textContent = p.arma_desc;
    document.getElementById('sel-hab').textContent = p.habilidad;
    document.getElementById('sel-hab-desc').textContent = p.habilidad_desc;
    const r = document.getElementById('sel-rating');
    r.textContent = '★'.repeat(p.rating) + '☆'.repeat(5 - p.rating);
    r.setAttribute('aria-label', p.rating + ' de 5');

    document.getElementById('seleccion').scrollIntoView({ behavior: 'smooth' });
  });
});