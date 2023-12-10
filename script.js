//Solicitud GET para llevar al front

const URL= "http://127.0.0.1:5000/"

fetch(URL + 'productos')
    .then(function(response){
        if (response.ok){
            return response.json();

        } else{
            throw new Error('Error al obtener los productos')
        }
    })
 .then(function(data){
    let tablaProductos=document.getElementById('tablaProductos');

    for(let producto of data){
        let fila= document.createElement('tr');
        fila.innerHTML = '<td>' + producto.id+ '</td>'+ '<td>' +  producto.tipo+ '</td>'+ '<td>'+  producto.marca + '</td>'+ '<td>'+  producto.modelo + '</td>'+ '<td>'+  producto.precio + '</td>'+ '<td>'+  producto.stock + '</td>'+ '<td>'+  producto.imagen+ '<td>';
        tablaProductos.appendChild(fila);
    
    }
    })  
    .catch(function(error){
        alert('Error al agregar los productos');
        console.error('Error:error');
    }) 

// Agregar un producto nuevo
document.getElementById('Formulario').addEventListener('submit', function(event){
    event.preventDefault();

    var formData= new FormData();
    formData.append('tipo',document.getElementById('tipo').value);
    formData.append('marca',document.getElementById('marca').value);
    formData.append('modelo',document.getElementById('modelo').value);
    formData.append('precio',document.getElementById('precio').value);
    formData.append('cantidad',document.getElementById('cantidad').value);
    formData.append('imagen',document.getElementById('imagen').value);

    fetch (URL + 'productos', {
        method: 'POST',
        body: formData
    })
    .then(function(response){
        if(response.ok){
            return response.json();
        } else{
            throw new Error ('Error al agregar el producto');
        }
    })
    .then (function(){
        alert('Producto agregado correctamente');
    })
    .catch(function(error){
        alert('Error al agregar el producto');
        console.error('Error:', error);
    })
})

