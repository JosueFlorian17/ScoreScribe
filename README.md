# ScoreScribe

ScoreScribe es un intérprete de lenguaje para la generación de partituras musicales en formato PDF y archivos de audio en formato WAV. Con este proyecto, puedes escribir música utilizando un lenguaje simple y convertirlo en partituras visuales y sonidos reproducibles.

## Características

- Convierte un lenguaje específico en partituras en formato PDF.
- Genera audio en formato WAV a partir de las partituras.
- Flexible y fácil de usar para músicos, compositores y desarrolladores.
- Soporte para distintas notaciones musicales y dinámicas.

## Requisitos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

- Python 3.8 o superior
- LilyPond (para la generación de partituras)
- Fluidsynth (para la generación de audio WAV)
- Las siguientes bibliotecas de Python:
  - `reportlab` (para el manejo de PDFs)
  - `midi2audio` (para convertir MIDI a WAV)
  - `numpy` (para procesamiento interno)

Puedes instalar las dependencias de Python usando:

```bash
pip install -r requirements.txt
