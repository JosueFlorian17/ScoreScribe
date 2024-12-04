document.getElementById('compilarBtn').addEventListener('click', function() {
    const codigo = document.getElementById('codigo').value;
  
    if (!codigo.trim()) {
      alert('Por favor, ingresa tu código primero.');
      return;
    }

    // Mostrar los botones de descarga después de compilar
    const descargas = document.getElementById('descargas');
    descargas.style.display = 'block';  // Mostrar los botones de descarga


});

document.getElementById('compilarBtn').addEventListener('click', function() {
    const codigo = document.getElementById('codigo').value;

    if (!codigo.trim()) {
        alert('Por favor, ingresa tu código primero.');
        return;
    }

    // Mostrar un mensaje mientras procesamos el código
    alert('Compilando el código, por favor espera...');

    // Enviar el código al servidor
    fetch('/compilar', {
        method: 'POST',
        body: new FormData().append('codigo', codigo)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Error: ' + data.error);
            return;
        }

        // Mostrar los botones de descarga
        const descargas = document.getElementById('descargas');
        descargas.style.display = 'block';  // Mostrar los botones de descarga

        // Actualizar los enlaces de descarga
        const archivosGenerados = data.archivos.map(archivo => {
            return `<a href="${archivo}" download>
                        <button class="descargar-btn">
                            Descargar ${archivo.split('/').pop()}
                        </button>
                    </a>`;
        }).join('');

        document.getElementById('archivosGenerados').innerHTML = archivosGenerados;
    })
    .catch(error => {
        alert('Hubo un error al compilar el código: ' + error);
    });
});
