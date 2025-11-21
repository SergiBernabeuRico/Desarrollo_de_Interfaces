# ejercicio2.py
# Ejemplo de una ventana con un QHBoxLayout y 4 botones en horizontal

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("QHBoxLayout")
        # Medidas de la ventana
        self.resize(300, 200)

        # Creamos y organizamos los widgets
        self.crear_interfaz()

    def crear_interfaz(self):
        # Creamos el Layout horizontal
        layout = QHBoxLayout()

        # Ajustamos márgenes y separación entre los widgets
        layout.setContentsMargins(20, 20, 20, 20)               # izquierda, arriba, derecha, abajo
        layout.setSpacing(10)                                   # espacion entre los botones

        # Creamos los botones con el texto correspondiente
        boton1 = QPushButton("Botó 1")
        boton2 = QPushButton("Botó 2")
        boton3 = QPushButton("Botó 3")
        boton4 = QPushButton("Botó 4")

        # Añadimos los botones al layout en posición horizontal
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        # Asignamos el Layout al la ventana
        self.setLayout(layout)

if __name__ == "__main__":
    # Creamos la aplicación
    app = QApplication(sys.argv)

    # Creamos y mostramos la ventana principal
    ventana = VentanaPrincipal()
    ventana.show()

    # Iniciamos el bucle de eventos de la aplicación
    sys.exit(app.exec())