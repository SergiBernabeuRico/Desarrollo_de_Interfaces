# Ejercicio1.py
# Ejemplo de una ventana con un QVBoxLayout y 4 botones en vertical

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana
        self.setWindowTitle("QVBoxLayout")
        # Configuramos el tamaño de la ventana
        self.resize(300, 200)

        # Llamamo al metodo que crea y organiza los widgets
        self.crear_interfaz()

    def crear_interfaz(self):
        # Creamos el Layout vertical
        layout = QVBoxLayout()

        # Ajustamos márgenes y separación entre widgets
        layout.setContentsMargins(20, 20, 20, 20)           # izquierda, arriba, derecha, abajo
        layout.setSpacing(10)                               # espacion entre los botones

        # Creamos los botones con el texto correspondiente
        boton1 = QPushButton("Botó 1")
        boton2 = QPushButton("Botó 2")
        boton3 = QPushButton("Botó 3")
        boton4 = QPushButton("botó 4")

        # Añadimos los botones al layout en orden vertical
        layout.addWidget(boton1)
        layout.addWidget(boton2)
        layout.addWidget(boton3)
        layout.addWidget(boton4)

        # Asignamos el layout a la ventana
        self.setLayout(layout)

if __name__ == "__main__":
    # Creamos la app
    app = QApplication(sys.argv)

    # Creamos y mostramos la ventana
    ventana = VentanaPrincipal()
    ventana.show()

    # Iniciamos el bucle de eventos de la app
    sys.exit(app.exec())


    