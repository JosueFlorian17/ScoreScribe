import os
import subprocess

# Mapa de letras a notas musicales
LETTER_TO_NOTE = {
    'a': 'c', 'b': 'd', 'c': 'e', 'd': 'f', 'e': 'g', 'f': 'a', 'g': 'b',
    'h': 'c', 'i': 'd', 'j': 'e', 'k': 'f', 'l': 'g', 'm': 'a', 'n': 'b',
    'o': 'c', 'p': 'd', 'q': 'e', 'r': 'f', 's': 'g', 't': 'a', 'u': 'b',
    'v': 'c', 'w': 'd', 'x': 'e', 'y': 'f', 'z': 'g'
}

def word_to_lilypond(word):
    """Convierte una palabra en un código de LilyPond."""
    notes = [LETTER_TO_NOTE.get(char.lower(), 'c') for char in word]
    return f"""
\\version "2.24.0"
\\score {{
    \\relative c' {{
        \\clef treble
        \\key c \\major
        \\time 4/4
        {' '.join(notes)}
    }}
    \\layout {{}}  % Asegura que el PDF se genere
    \\midi {{
        \\tempo 4=120  % Configura un tempo para evitar problemas
    }}
}}
"""

def create_lilypond_file(word, lilypond_path, output_path):
    """Genera el archivo .ly, el PDF, el MIDI y el WAV."""
    # Generar código de LilyPond
    lilypond_code = word_to_lilypond(word)
    
    # Rutas de los archivos
    ly_file = os.path.join(output_path, f"{word}.ly")
    pdf_file = os.path.join(output_path, f"{word}.pdf")
    midi_file = os.path.join(output_path, f"{word}.mid")  # Cambié la extensión a .mid
    wav_file = os.path.join(output_path, f"{word}.wav")

    # Guardar el archivo .ly
    with open(ly_file, "w") as file:
        file.write(lilypond_code)
    
    # Compilar con LilyPond
    try:
        subprocess.run([lilypond_path, ly_file], check=True)
        print(f"PDF generado: {pdf_file}")
        print(f"MIDI generado: {midi_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al compilar LilyPond: {e}")
        return

    # Usar TiMidity++ para generar el archivo WAV
    timidity_exe = r"C:\Users\Florian\OneDrive\Escritorio\ilp\TiMidity++-2.15.0\timidity.exe"  # Ruta completa al ejecutable de TiMidity++
    try:
        # Construir y ejecutar el comando para TiMidity++
        command = [
            timidity_exe, 
            os.path.abspath(midi_file),  # Ruta absoluta al archivo MIDI
            "-Ow", 
            "-o", 
            os.path.abspath(wav_file)  # Ruta absoluta al archivo WAV
        ]
        subprocess.run(command, check=True)
        print(f"WAV generado: {wav_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al generar WAV con TiMidity++: {e}")


if __name__ == "__main__":
    # Ruta al ejecutable de LilyPond
    lilypond_exe = r"C:\Users\Florian\OneDrive\Escritorio\ilp\lilypond-2.24.4\bin\lilypond.exe"
    
    # Carpeta de salida
    output_directory = r"C:\Users\Florian\OneDrive\Escritorio\ilp"  # Carpeta de salida configurada explícitamente
    os.makedirs(output_directory, exist_ok=True)
    
    # Pedir una palabra al usuario
    palabra = input("Ingresa una palabra para convertir en melodía: ")
    
    # Generar los archivos
    create_lilypond_file(palabra, lilypond_exe, output_directory)
