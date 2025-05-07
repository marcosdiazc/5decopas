/* /static/menu.js */
const burger = document.getElementById("burger");
const navUl  = document.getElementById("nav-ul");

if (burger && navUl) {
  burger.addEventListener("click", () => {
    navUl.classList.toggle("open");      // muestra / oculta
    burger.classList.toggle("active");   // anima el ícono
  });
}

