from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import subprocess

app = Flask(__name__)

# Directorio donde se guardarán los archivos generados
OUTPUT_DIR = './'


# Ruta para renderizar el index.html
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para recibir el código y ejecutar el proceso
@app.route('/compilar', methods=['POST'])
def compilar():
    codigo = request.form.get('codigo')  # Obtener el código enviado desde el frontend

    if not codigo:
        return jsonify({'error': 'No se ha enviado código'}), 400

    # Guardar el código en un archivo .alg
    musica_path = os.path.join(OUTPUT_DIR, 'musica.alg')
    with open(musica_path, 'w') as f:
        f.write(codigo)

    # Ejecutar el script de Python
    try:
        subprocess.run(['python', '/algoritmia.py', musica_path], check=True)
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Hubo un error al ejecutar el script de Python', 'details': str(e)}), 500

    # Devolver los archivos generados (out.pdf, out.mid, out.wav)
    archivos = ['out.pdf', 'out.mid', 'out.wav']
    return jsonify({
        'archivos': [f'/descargar/{archivo}' for archivo in archivos]
    })


# Ruta para servir los archivos generados
@app.route('/descargar/<archivo>')
def descargar(archivo):
    return send_from_directory(OUTPUT_DIR, archivo)


if __name__ == '__main__':
    app.run(debug=True)
