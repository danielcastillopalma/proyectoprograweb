/*¨
swiper
*/

var swiper = new Swiper(".mySwiper", {

  spaceBetween: 20,
  rewind: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
    loop: true,
  },
  breakpoints: {
    360: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    640: {
      slidesPerView: 2,
      spaceBetween: 10,
    },
    768: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1024: {
      slidesPerView: 5,
      spaceBetween: 20,
    },
  },
});

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

  if (nombre.length<3) {
    errorNombre.innerText = "El largo del nombre debe ser mayor que 3";
    document.getElementById("errorNombre").hidden = false;
    return;
 }
 if (correo.length<6) {
  errorCorreo.innerText = "El largo del correo debe ser mayor que 6";
  document.getElementById("errorCorreo").hidden = false;
  return;
}

  is.submit();
};
