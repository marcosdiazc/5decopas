const burger = document.getElementById("burger");
const navUl  = document.getElementById("nav-ul");

burger.addEventListener("click", () => {
  navUl.classList.toggle("mobile-hidden");
  // animación cruz
  [...burger.children].forEach((bar, i) => {
    bar.style.transform = navUl.classList.contains("mobile-hidden")
      ? "rotate(0)"
      : i === 0
        ? "translateY(6px) rotate(45deg)"
        : i === 1
          ? "scaleX(0)"
          : "translateY(-6px) rotate(-45deg)";
  });
});
