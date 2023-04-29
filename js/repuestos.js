var posId = 1;
var cont = 0;
function cargarProductos() {
  let num = document.getElementById('up');
  num.setAttribute("num",1);
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
      document.getElementById('contenedorProdRep').innerHTML=html;
      return producto.idProd===20;
      });
    });
}
function page2() {
  let num = document.getElementById('up');
  num.setAttribute("num",2);
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
        if(producto.idProd>20){
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
      document.getElementById('contenedorProdRep').innerHTML=html;
        }
      return producto.idProd===40;
      });
    });
}
function page3() {
  let num = document.getElementById('up');
  num.setAttribute("num",3);
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
        if(producto.idProd>40){
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
      document.getElementById('contenedorProdRep').innerHTML=html;
        }
      var posId = producto.idProd;
      return producto.idProd===60;
      
      });
    });
}

function pagUp(){
  let num = document.getElementById('up');
  let actual = num.getAttribute('num');  
  num.setAttribute("num",parseInt(actual)+1);
  let sig  = num.getAttribute('num');
  
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
        if(producto.idProd>actual*20){
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
      document.getElementById('contenedorProdRep').innerHTML=html;
        }
      return producto.idProd===sig*20;
      });
    });
}
function pagDown(){
  let num = document.getElementById('up');
  let actual = num.getAttribute('num'); 
  num.setAttribute('num',parseInt(actual)-1); 
  let nueva = num.getAttribute('num'); 
  

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
        if(producto.idProd>(nueva-1)*20 && actual>1){
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
      document.getElementById('contenedorProdRep').innerHTML=html;
        }
      var posId = producto.idProd;
      return producto.idProd===nueva*20;
      
      });
    });

  
}

