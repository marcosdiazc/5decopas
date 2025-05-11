const API = "https://fivedecopas-backend.onrender.com/jugadores";
const tbody  = document.getElementById("tabla-jugadores");
const genero = document.getElementById("genero");
const equipo = document.getElementById("equipo");

async function fetchJugadores(){ 
  const r = await fetch(API); 
  return r.json(); 
}

function pintar(list){
  // Ordenar de mayor a menor por goles
  list.sort((a, b) => (b.goals ?? 0) - (a.goals ?? 0));

  tbody.innerHTML = list.map(j => `
    <tr>
      <td>${j.name}</td>
      <td>${j.position || '-'}</td>
      <td>${j.gender}</td>
      <td>${j.team}</td>
      <td>${j.goals ?? 0}</td>
      <td>${j.assistances ?? 0}</td>
      <td>${j.matches ?? 0}</td>
    </tr>
  `).join("");
}

async function filtrar(){
  const todos = await fetchJugadores();
  const out = todos.filter(j =>
    (!genero.value || j.gender === genero.value) &&
    (!equipo.value || j.team === equipo.value)
  );
  pintar(out);
}

document.getElementById("filtrar").onclick = filtrar;
document.getElementById("reset").onclick = async ()=>{
  genero.value = equipo.value = "";
  pintar(await fetchJugadores());
};

// Carga inicial
(async ()=> pintar(await fetchJugadores()))();
