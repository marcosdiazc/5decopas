const slider = document.getElementById("slider");
const slides = slider?.querySelectorAll("img") || [];
let index = 0;

function showSlide(i) {
  const total = slides.length;
  index = (i + total) % total;
  slider.style.transform = `translateX(-${index * 100}%)`;
}

if (slides.length > 0) {
  setInterval(() => {
    showSlide(index + 1);
  }, 4000);
}

