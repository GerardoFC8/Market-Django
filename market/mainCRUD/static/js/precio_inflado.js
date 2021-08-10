function precio_inflado(precio){
    document.querySelector(".precio_desc span").innerHTML = precio + (precio * 10 / 100);
    console.log(precio + (precio * 10 / 100));
}


