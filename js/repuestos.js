var posId = 1;
var cont = 0;
function cargarProductos() {
  const e1 = document.querySelector(".p1");
  e1.classList.add("activo");
  const e2 = document.querySelector(".p2");
  e2.classList.remove("activo");
  const e3 = document.querySelector(".p3");
  e3.classList.remove("activo");
  let num = document.getElementById("up");
  num.setAttribute("num", 1);
  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      console.log(data);
      data.some(function (producto) {
        html += `
        
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
              <h3>$${producto.idProd}</h3>
            </div>
          </div>
          
      `;
        document.getElementById("contenedorProdRep").innerHTML = html;
        return producto.idProd === 20;
      });
    });
}
function page2() {
  const e1 = document.querySelector(".p1");
  e1.classList.remove("activo");
  const e2 = document.querySelector(".p2");
  e2.classList.add("activo");
  const e3 = document.querySelector(".p3");
  e3.classList.remove("activo");
  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      console.log(data);
      data.some(function (producto) {
        if (producto.idProd > 20) {
          html += `
        
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
              <h3>$${producto.idProd}</h3>
            </div>
          </div>
          
      `;
          document.getElementById("contenedorProdRep").innerHTML = html;
        }
        return producto.idProd === 40;
      });
    });
}
function page3() {
  const e1 = document.querySelector(".p1");
  e1.classList.remove("activo");
  const e3 = document.querySelector(".p3");
  e3.classList.add("activo");
  const e2 = document.querySelector(".p2");
  e2.classList.remove("activo");

  $('div').blur();

  let num = document.getElementById("up");
  num.setAttribute("num", 3);

  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      console.log(data);
      data.some(function (producto) {
        if (producto.idProd > 40) {
          html += `
        
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
              <h3>$${producto.idProd}</h3>
            </div>
          </div>
          
      `;
          document.getElementById("contenedorProdRep").innerHTML = html;
        }
        var posId = producto.idProd;
        return producto.idProd === 60;
      });
    });
}

function pagUp() {
  let num = document.getElementById("up");
  let actual = num.getAttribute("num");
  num.setAttribute("num", parseInt(actual) + 1);
  let sig = num.getAttribute("num");

  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      console.log(data);
      data.some(function (producto) {
        if (producto.idProd > actual * 20) {
          html += `
        
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
              <h3>$${producto.idProd}</h3>
            </div>
          </div>
          
      `;
          document.getElementById("contenedorProdRep").innerHTML = html;
        }
        return producto.idProd === sig * 20;
      });
    });
}
function pagDown() {
  let num = document.getElementById("up");
  let actual = num.getAttribute("num");
  num.setAttribute("num", parseInt(actual) - 1);
  let nueva = num.getAttribute("num");

  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      let html = "";
      console.log(data);
      data.some(function (producto) {
        if (producto.idProd > (nueva - 1) * 20 && actual > 1) {
          html += `
        
          <div class="card" style="width: 18rem;">
            <img src=${producto.imgSrc} class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">${producto.nomProd}</h5>
              <p class="card-text">${producto.descProd}</p>
              <h3>$${producto.idProd}</h3>
            </div>
          </div>
          
      `;
          document.getElementById("contenedorProdRep").innerHTML = html;
        }
        var posId = producto.idProd;
        return producto.idProd === nueva * 20;
      });
    });
}
