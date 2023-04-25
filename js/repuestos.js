
const contenedorProductos = document.querySelector(".productosRepuestos");

function fetchProducto(idCategory) {
  fetch(`https://fakestoreapi.com/products/${idCategory}/`)
    .then((res) => res.json())
    .then((data) => console.log(data));
}

function fetchProductos(numero){
    for(i=1;i<=numero;i++){
        fetchProducto(i);
    }
}
fetchProductos(10);
