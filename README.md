# Juego de Culebrita

Este es un sencillo juego de la culebrita (Snake) desarrollado en Python utilizando la librería PyGame. El juego incluye un menú de inicio con tres niveles de dificultad (Novato, Intermedio y Avanzado) y un menú de fin del juego con opciones para reiniciar o volver al menú principal.

## Requisitos

- Python 3.x
- PyGame

## Instalación

1. Navega al directorio del proyecto:

    ```sh
    cd PyGame
    ```

2. Instala las dependencias necesarias:

    ```sh
    pip install pygame
    ```

## Implementación
Para correr el juego, simplemente corre en la terminal del proyecto `Proyecto.py`:

```sh
python Proyecto.py
```

## Controles

- Usa las teclas de dirección (flechas) para mover la culebrita.
- En el menú de inicio:
   - Presiona 1 para jugar en dificultad  "Novato".
   - Presiona 2 para jugar en dificultad  "Intermedio".
   - Presiona 3 para jugar en dificultad  "Avanzado".

- En el menú de fin del juego:
    - Presiona 1 para reintentar el nivel actual.
    - Presiona 2 para volver al menú principal.


## Niveles de Dificultad

- Novato: Velocidad de la culebrita lenta.
- Intermedio: Velocidad de la culebrita media.
- Avanzado: Velocidad de la culebrita rápida y obstáculos adicionales en el campo de juego.

## Funciones del Juego

- Menú de Inicio: Selección de niveles de dificultad.
- Obstáculos (Nivel Avanzado): Obstáculos rojos que aparecen en el campo de juego.
- Menú de Fin del Juego: Muestra la puntuación y permite reintentar o volver al menú principal.
- Puntuación en tiempo real: La puntuación se muestra en la esquina superior izquierda durante el juego.