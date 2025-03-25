document.addEventListener("DOMContentLoaded", () => {
    const carritoIcono = document.querySelector(".carrito");
    const botonesAgregar = document.querySelectorAll(".producto button");
    const carritoModal = document.createElement("div");
    
    let carrito = [];

    // Crear el modal del carrito
    carritoModal.classList.add("carrito-modal");
    document.body.appendChild(carritoModal);

    carritoIcono.addEventListener("click", () => {
        mostrarCarrito();
    });

    botonesAgregar.forEach((boton, index) => {
        boton.addEventListener("click", () => {
            agregarAlCarrito(index);
        });
    });

    function agregarAlCarrito(index) {
        const producto = document.querySelectorAll(".producto")[index];
        const nombre = producto.querySelector("h3").textContent;
        const precio = producto.querySelector("p").textContent;
        const imagen = producto.querySelector("img").src;

        const item = {
            nombre,
            precio,
            imagen,
            cantidad: 1
        };

        const existe = carrito.find(p => p.nombre === nombre);
        if (existe) {
            existe.cantidad++;
        } else {
            carrito.push(item);
        }
        
        actualizarCarrito();
    }

    function actualizarCarrito() {
        localStorage.setItem("carrito", JSON.stringify(carrito));
        mostrarCarrito();
    }

    function mostrarCarrito() {
        carritoModal.innerHTML = `<h2>Carrito de Compras</h2>`;
        if (carrito.length === 0) {
            carritoModal.innerHTML += `<p>Tu carrito está vacío.</p>`;
        } else {
            carrito.forEach((item, index) => {
                carritoModal.innerHTML += `
                    <div class="item-carrito">
                        <img src="${item.imagen}" width="50">
                        <span>${item.nombre} - ${item.precio} x${item.cantidad}</span>
                        <button class="eliminar" data-index="${index}">❌</button>
                    </div>`;
            });
            carritoModal.innerHTML += `<button class="vaciar">Vaciar Carrito</button>`;
        }

        document.querySelectorAll(".eliminar").forEach(btn => {
            btn.addEventListener("click", (e) => {
                const index = e.target.getAttribute("data-index");
                carrito.splice(index, 1);
                actualizarCarrito();
            });
        });

        const btnVaciar = document.querySelector(".vaciar");
        if (btnVaciar) {
            btnVaciar.addEventListener("click", () => {
                carrito = [];
                actualizarCarrito();
            });
        }
    }

    if (localStorage.getItem("carrito")) {
        carrito = JSON.parse(localStorage.getItem("carrito"));
        mostrarCarrito();
    }
});
