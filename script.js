const URL = "http://127.0.0.1:5000/";

// Función para crear un botón de eliminar
function createDeleteButton(productId) {
    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Eliminar';
    deleteButton.addEventListener('click', function() {
        deleteProduct(productId);
    });
    return deleteButton;
}
// Función para eliminar un producto
function deleteProduct(productId) {
    fetch(URL + 'productos/' + productId, {
        method: 'DELETE',
    })
    .then(function (response) {
        if (response.ok) {
            alert('Producto eliminado correctamente');
            // Puedes actualizar la tabla aquí si es necesario
        } else {
            throw new Error('Error al eliminar el producto');
        }
    })
    .catch(function (error) {
        alert('Error al eliminar el producto');
        console.error('Error:', error);
    });
}

// Función para crear un botón de editar
function createEditButton(productId) {
    const editButton = document.createElement('button');
    editButton.textContent = 'Editar';
    editButton.addEventListener('click', function() {
        window.location.href = 'editar.html?id=' + productId;
        // Redirige a la página 'editar.html' con el ID del producto como parámetro en la URL
    });
    return editButton;
}


// Funcion para listar productos
fetch(URL + 'productos')
    .then(function (response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error al obtener los productos');
        }
    })
    .then(function (data) {
        let tablaProductos = document.getElementById('tablaProductos');

        for (let producto of data) {
            let fila = document.createElement('tr');
            fila.innerHTML = '<td>' + producto.id + '</td>' + '<td>' + producto.tipo + '</td>' + '<td>' + producto.marca + '</td>' + '<td>' + producto.modelo + '</td>' + '<td>' + producto.precio + '</td>' + '<td>' + producto.stock + '</td>' + '<td>' + producto.imagen + '</td>';

            // Agregar botón de editar a la fila
            const editButton = createEditButton(producto.id);
            fila.appendChild(editButton);

            // Agregar botón de eliminar a la fila
            const deleteButton = createDeleteButton(producto.id);
            fila.appendChild(deleteButton);

            tablaProductos.appendChild(fila);
        }
 })
    .catch(function (error) {
        alert('Error al obtener los productos');
        console.error('Error:', error);
    });
    document.getElementById('formulario').addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que el formulario se envíe de forma tradicional
    
        // Obtener los valores del formulario
        const tipo = document.getElementById('tipo').value;
        const marca = document.getElementById('marca').value;
        const modelo = document.getElementById('modelo').value;
        const cantidad = document.getElementById('cantidad').value;
        const precio = document.getElementById('precio').value;
        const imagen = document.getElementById('imagen').value;
    
        // Crear objeto con los datos del nuevo producto
        const nuevoProducto = {
            tipo: tipo,
            marca: marca,
            modelo: modelo,
            stock: cantidad,
            precio: precio,
            imagen: imagen
        };
    
        // Enviar la solicitud POST al servidor
        fetch(URL + 'productos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevoProducto)
        })
        .then(function(response) {
            if (response.ok) {
                console.log('Solicitud de agregar producto enviada correctamente');
                return response.json();
            } else {
                throw new Error('Error al enviar solicitud para agregar producto');
            }
        })
        .then(function(data) {
            // Puedes hacer algo con la respuesta del servidor si es necesario
        })
        .catch(function(error) {
            console.error('Error:', error);
        });
});
function buscarProductos() {
    const tipoBusqueda = document.getElementById('tipoBusqueda').value.toLowerCase();
    const marcaBusqueda = document.getElementById('marcaBusqueda').value.toLowerCase();

    fetch(URL + 'productos')
        .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error al obtener los productos');
            }
        })
        .then(function (data) {
            let tablaProductos = document.getElementById('tablaProductos');
            tablaProductos.innerHTML = '';

            for (let producto of data) {
                if (producto.tipo.toLowerCase().includes(tipoBusqueda) && producto.marca.toLowerCase().includes(marcaBusqueda)) {
                    let fila = document.createElement('tr');
                    fila.innerHTML = '<td>' + producto.id + '</td>' + '<td>' + producto.tipo + '</td>' + '<td>' + producto.marca + '</td>' + '<td>' + producto.modelo + '</td>' + '<td>' + producto.precio + '</td>' + '<td>' + producto.stock + '</td>' + '<td>' + producto.imagen + '</td>';

                    const editButton = createEditButton(producto.id);
                    fila.appendChild(editButton);

                    const deleteButton = createDeleteButton(producto.id);
                    fila.appendChild(deleteButton);

                    tablaProductos.appendChild(fila);
                }
            }
        })
        .catch(function (error) {
            alert('Error al obtener los productos');
            console.error('Error:', error);
        });
}

// funcion editar producto
fetch(URL + 'productos/' + productId, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json' // Asegúrate de tener este encabezado
    },
    body: JSON.stringify(datosActualizadosDelProducto) // Aquí debes enviar los datos actualizados del producto
})