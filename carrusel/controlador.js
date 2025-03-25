let indice = 0;
        mostrarProducto(indice);
        
        function mostrarProducto(n) {
            let productos = document.getElementsByClassName("producto");
            for (let i = 0; i < productos.length; i++) {
                productos[i].style.display = "none";
            }
            productos[n].style.display = "block";
        }
        
        function cambiarProducto(n) {
            let productos = document.getElementsByClassName("producto");
            indice = (indice + n + productos.length) % productos.length;
            mostrarProducto(indice);
        }