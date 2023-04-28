function cargarProductos() {
  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      data.forEach(function (producto) {
        html += `
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
            </div>
          </div>
      `;
      document.getElementById('contenedorProdRep').innerHTML=html;
      });
    });
}
cargarProductos();
