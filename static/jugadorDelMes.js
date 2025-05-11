document.getElementById("ver-jugador-del-mes").onclick = () => {
    const seccion = document.getElementById("jugador-del-mes");
    seccion.style.display = "block";
    seccion.scrollIntoView({ behavior: "smooth" });
  };
  