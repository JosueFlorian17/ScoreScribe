# converter.py

import os
import subprocess

# Mapa de letras a notas musicales
LETTER_TO_NOTE = {
    "a0": "a,,,", "b0": "b,,,",
    "c1": "c,,", "d1": "d,,", "e1": "e,,", "f1": "f,,", "g1": "g,,", "a1": "a,,", "b1": "b,,",
    "c2": "c,", "d2": "d,", "e2": "e,", "f2": "f,", "g2": "g,", "a2": "a,", "b2": "b,",
    "c3": "c", "d3": "d", "e3": "e", "f3": "f", "g3": "g", "a3": "a", "b3": "b",
    "c": "c'", "d": "d'", "e": "e'", "f": "f'", "g": "g'", "a": "a'", "b": "b'",
    "c5": "c''", "d5": "d''", "e5": "e''", "f5": "f''", "g5": "g''", "a5": "a''", "b5": "b''",
    "c6": "c'''", "d6": "d'''", "e6": "e'''", "f6": "f'''", "g6": "g'''", "a6": "a'''", "b6": "b'''",
    "c7": "c''''", "d7": "d''''", "e7": "e''''", "f7": "f''''", "g7": "g''''", "a7": "a''''", "b7": "b''''",
    "c8": "c'''''"
}

def word_to_lilypond(notes_list):
    """Convierte una lista de notas en un código de LilyPond, procesando cada nota."""
    # Convertir las notas a minúsculas y mapearlas
    notes = [LETTER_TO_NOTE.get(note.lower(), 'c') for note in notes_list]

    return f"""
\\version "2.24.0"
\\score {{
    {{
        {' '.join(notes)}  % Aquí todas las notas juntas en orden
    }}
    \\layout {{}}  % Asegura que el PDF se genere
    \\midi {{
        \\tempo 4=120  % Configura un tempo para evitar problemas
    }}
}}
"""

def create_lilypond_file(notes_list, lilypond_path, timidity_path, output_path):
    """Genera el archivo .ly, el PDF, el MIDI y el WAV para la secuencia de notas."""
    lilypond_code = word_to_lilypond(notes_list)

    # Aseguramos que los archivos se guarden en el directorio actual (output_path es el directorio actual)
    ly_file = os.path.join(output_path, "out.ly")
    pdf_file = os.path.join(output_path, "out.pdf")
    midi_file = os.path.join(output_path, "out.mid")
    wav_file = os.path.join(output_path, "out.wav")

    # Verificación de las rutas de salida
    print(f"Archivos se generarán en: {output_path}")
    print(f"Archivo .ly: {ly_file}")
    print(f"Archivo .pdf: {pdf_file}")
    print(f"Archivo .midi: {midi_file}")
    print(f"Archivo .wav: {wav_file}")

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
    try:
        command = [
            timidity_path,
            os.path.abspath(midi_file),  # Asegura que la ruta sea absoluta
            "-Ow",
            "-o",
            os.path.abspath(wav_file)  # Asegura que la ruta sea absoluta
        ]
        subprocess.run(command, check=True)
        print(f"WAV generado: {wav_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al generar WAV con TiMidity++: {e}")
