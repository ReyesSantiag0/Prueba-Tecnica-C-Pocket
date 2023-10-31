let idObjeto = 1;

// Función para agregar los datos en la tabla
function agregarDato() {
  let nombre_objeto = document.getElementById("nombre_objeto").value;
  let categoria_objeto = document.getElementById("categoria_objeto").value;

  if (nombre_objeto && categoria_objeto) {
    let tabla = document.getElementById("tablaDatos");
    let newRow = tabla.insertRow(tabla.rows.length);

    let cellId = newRow.insertCell(0);
    let cellNombre = newRow.insertCell(1);
    let cellCategoria = newRow.insertCell(2);
    let cellAcciones = newRow.insertCell(3);

    cellId.innerHTML = idObjeto;
    cellNombre.innerHTML = nombre_objeto;
    cellCategoria.innerHTML = categoria_objeto;
    cellAcciones.innerHTML =
      '<button class="btn btn-danger btn-sm" onclick="eliminarDato(this)">Eliminar</button>';
    idObjeto++;

    document.getElementById("nombre_objeto").value = "";
    document.getElementById("categoria_objeto").value = "";
  } else {
    alert("Por favor, ingresa un nombre y una categoría.");
  }
}

// Función para eliminar los datos registrados en la tabla
function eliminarDato(button) {
  var row = button.closest("tr");
  row.parentNode.removeChild(row);
}
