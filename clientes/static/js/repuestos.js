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
              <h3>$${producto.valorProd}</h3>
              <button class="btnMas csecundario clink" id="${producto.idProd}" onclick="agregar(this)"><i class="fa-duotone fa-plus fa-beat"></i></button>
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
              <h3>$${producto.valorProd}</h3> 
              <button class="btnMas cprimario  clink" id="${producto.idProd}" onclick="agregar(this)"><i class="fa-duotone fa-plus fa-beat"></i></button>
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

  $("div").blur();

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
              <h3>$${producto.valorProd}</h3>
              <button class="btnMas csecundario  clink" id="${producto.idProd}" onclick="agregar(this)"><i class="fa-duotone fa-plus fa-beat"></i></button>
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
              <h3>$${producto.valorProd}</h3>
              <button class="btnMas csecundario  clink" id="${producto.idProd}" onclick="agregar(this)"><i class="fa-duotone fa-plus fa-beat"></i></button>
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
              <h3>$${producto.valorProd}</h3>
              <button class="btnMas csecundario  clink" id="${producto.idProd}" onclick="agregar(this)"><i class="fa-duotone fa-plus fa-beat"></i></button>
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

/*
arreglar codigo de abajo
*/

function agregar(produId) {
  let id = produId.id;
  console.log(id);

  fetch(
    "https://raw.githubusercontent.com/danielcastillopalma/api/master/db.json"
  )
    .then(function (res) {
      return res.json();
    })
    .then(function (data) {
      for (var prodId in data) {
        console.log(" name=" + prodId + " value=" + data[id]);
        if (prodId === id) {
          return;
        }
      }
    });
}
/*


*/

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

let btns = document.querySelectorAll(".repuestosContainer button");
btns.forEach((btn) => {
  btn.addEventListener("click", addToCart);
});

function addToCart(e) {
  let id_prod = e.target.value;
  let url = "/clientes/add_to_cart";
  let data = { id: id_prod };
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("num_of_items").innerHTML = data
      console.log(data)
    })
    .catch((error) => {
      console.log(error);
    });
}
let btnos = document.querySelectorAll(".filaCarrito button");
btnos.forEach((btn) => {
  btn.addEventListener("click", removeFromCart);
});

function removeFromCart(e) {
  let id_prod = e.target.value;
  let url = "/clientes/remove_from_cart";
  let data = { id: id_prod };
  let idd="quantity"+id_prod
  console.log(id_prod)
  console.log(idd)
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "X-CSRFToken": csrftoken },
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("num_of_items").innerHTML = data
      document.getElementById(idd).innerHTML = data
      console.log(data)
    })
    .catch((error) => {
      console.log(error);
    });
}