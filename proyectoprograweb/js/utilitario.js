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
$("input[name=correo]").on("invalid", function() {
  this.setCustomValidity("Ingrese un correo valido porfavor");
});
