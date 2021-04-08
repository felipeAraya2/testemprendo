function validarNombre() {
    var nom = document.getElementById("txtNombre").value;
    var largo = nom.trim().length;
    if (largo >= 2 ) {
        return true;
    } else {

        return false;
    }
}

function validarTodo() {
    var resp;
    resp = validarNombre();
    if (resp == false) {
        alert("el nombre debe tener más de 2 caracteres")
        return false;
    }
    
}

function validarNombreC() {
    var nom = document.getElementById("txtNombreCat").value;
    var largo = nom.trim().length;
    if (largo >= 2 ) {
        return true;
    } else {

        return false;
    }
}
function validarCat() {
    var resp;
    resp = validarNombreC();
    if (resp == false) {
        alert("el nombre debe tener más de 2 caracteres")
        return false;
    }
    
}

