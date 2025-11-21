# Ejercicio 7
# Representación de un tablero de ajedrez usando QGridLayout

import sys 
from PySide6.QtWidgets import (QApplication, QWidget, QGridLayout, QFrame)

class tablero(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("Tablero de ajedrez")

        # Ajustamos tamaño del tablero (60px por lado de casilla, 8 casillas cada fila y 8 casillas cada columna)
        self.resize(480, 480)

        # Crear y organizar interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Creamos layout de tipo cuadrícula
        grid = QGridLayout()

        # Ajustamos los márgenes y separación entre las casillas
        grid.setContentsMargins(0, 0, 0, 0)     # (arriba, izquierda, bajo , derecha)
        grid.setSpacing(0)                      # Sin espacio entre casillas para que se vean pegadas

        # Tamaño de cada casilla en (en píxeles)
        tam_casilla = 60

        # Creamos 8 filas X 8 columnas
        for fila in range(8):
            for columna in range(8):
                # Creamos un QFrame para usarlo como casilla
                casilla = QFrame()
                casilla.setFixedSize(tam_casilla, tam_casilla)

                # Añadimos un marco para ver mejor los bordes
                casilla.setFrameShape(QFrame.Box)

                # Alternamos el color blanco y el negro 
                # Si la suma de fila + columna es par -> blanco, si es impar -> negro
                if (fila + columna) % 2 == 0:
                    casilla.setStyleSheet("background-color: white;")
                else:
                    casilla.setStyleSheet("background-color: black;")

                # Añadimos la casilla a la cuadrícula
                grid.addWidget(casilla, fila, columna)

        # Asignamos el layout a la ventana
        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = tablero()
    ventana.show()

    sys.exit(app.exec())


