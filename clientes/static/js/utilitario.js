/*
forms
*/

document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("formulario")
    .addEventListener("submit", validarFormulario);
});



function validarFormulario(evento) {
  evento.preventDefault();

  var nombre = document.getElementById("nombre").value.trim();
  var correo = document.getElementById("correo").value;
  var telefono = document.getElementById("telefono").value;
  var mensajeContacto = document.getElementById("mensajeContacto").value;

  var errorNombre = document.getElementById("errorNombre");

  var validarEmail= /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/ ;

  if (nombre.length < 3) {
    errorNombre.innerText = "El largo del nombre debe ser mayor que 3";
    document.getElementById("errorNombre").hidden = false;
    return;
  }else{
    document.getElementById("errorNombre").hidden = true;
  }
  if (validarEmail.test(correo)) {
    document.getElementById("errorCorreo").hidden = true;
   
  }else{
    errorCorreo.innerText = "El formato del correo debe ser correo@dominio.com";
    document.getElementById("errorCorreo").hidden = false;
    return;
  }
  if(telefono.length!=9){
    errorTelefono.innerText="El largo del telefono debe ser de 9 numeros"
    document.getElementById("errorTelefono").hidden = false;
    return;
  }else{
    document.getElementById("errorTelefono").hidden = true;
  }
  alert("Mensaje enviado de forma exitosa");

  this.submit();
};

$('#correoLogin').on('focusout',function(){
  var texto = $(this).val();
  if(texto.length > 0 && texto.match(/^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/))
      $('#correoLogin').addClass('is-valid')
  else
      $('#correoLogin').addClass('is-invalid')
});
$('#passwordLogin').on('focusout',function(){
  var texto = $(this).val();
  if(texto.length > 0 )
      $('#passwordLogin').addClass('is-valid')
  else
      $('#passwordLogin').addClass('is-invalid')
});
