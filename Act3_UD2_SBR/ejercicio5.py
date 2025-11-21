# Ejercicio 5
# Ventana con QGridLayout que organiza los botones como en la imagen

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QGridLayout)

class VentanaCuadricula(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("QGridLayout")
        # Tamaño aproximado
        self.resize(400,200)

        # Crear y organizar los widgets
        self.crear_interfaz()

        # Crear y organizar interfazç
    def crear_interfaz(self):
        # Creamos el layuot de tipo cuadrícula
        grid = QGridLayout()

        # --- Fila 0: cuatro botones individuales ---
        btn_1 = QPushButton("0,0")
        btn_2 = QPushButton("0,1")
        btn_3 = QPushButton("0,2")
        btn_4 = QPushButton("0,3")
        # Cada botón ocupa su celda (fila, columna)
        grid.addWidget(btn_1, 0, 0)
        grid.addWidget(btn_2, 0, 1)
        grid.addWidget(btn_3, 0, 2)
        grid.addWidget(btn_4, 0, 3)

        # --- Fila 1: un botón que ocupa de la columna 0 a la 3 ---
        btn_5 = QPushButton("1, 0-3")
        # addWidget (widget, fila, columna, filasQueOcupa, columnasQueOcupa)
        grid.addWidget(btn_5, 1, 0, 1, 4) # 1 fila, 4 columnas

        # --- Fila 2: dos botones que ocupan dos columnas cada uno ---
        btn_6 = QPushButton("2, 0-1")
        btn_7 = QPushButton("2, 2-3")
        # Primer botón: fila 2, columna 0, ocupa 1 fila y dos columnas (0 y 1)
        grid.addWidget(btn_6, 2, 0, 1, 2)
        # Segundo botón: fila 2, columna 2, ocupa 1 fila y 2 columnas (2 y 3)
        grid.addWidget(btn_7, 2, 2, 1, 2)

        # Ajustamos márgenes y separación para que se parezaca a la imagen
        grid.setContentsMargins(20, 20, 20, 20)
        grid.setSpacing(10)

        # Asignamos el layout a la ventana
        self.setLayout(grid)

if __name__ =="__main__":
    app = QApplication(sys.argv)

    ventana = VentanaCuadricula()
    ventana.show()

    sys.exit(app.exec())


        
