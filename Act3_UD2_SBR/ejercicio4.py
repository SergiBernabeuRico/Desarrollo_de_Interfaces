# Ejercicio 4
# QTabWidget con 4 pestañas de colores (amarillo, azul, verde y rojo) en el lateral

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QTabWidget, QVBoxLayout)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("QTabWidget")
        # Tamaño de la ventan
        self.resize(600, 400)

        # Crear y organizar la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Layout principal de la ventana
        ventana_colores = QVBoxLayout()

        # --- QTabWidgets (contenedor de pestañas) ---
        self.tabs = QTabWidget()
        # Colocamos las pestañas en el lado izquierdo (vertical)
        self.tabs.setTabPosition(QTabWidget.West)

         # Creamos los 4 widgets, uno por pestaña, cada uno con un color de fondo
        # Solo necesitamos un QWidget por pestaña y le aplicamos un estilo CSS

        # Pestaña amarilla
        tab_yellow = QWidget()
        tab_yellow.setStyleSheet("background-color: yellow;")
        self.tabs.addTab(tab_yellow, "groc")

        # Pestaña azul
        tab_blue = QWidget()
        tab_blue.setStyleSheet("background-color: blue;")
        self.tabs.addTab(tab_blue, "blau")

        # Pestaña verde
        tab_green = QWidget()
        tab_green.setStyleSheet("background-color: green;")
        self.tabs.addTab(tab_green, "verd")

        # Pestaña roja
        tab_red = QWidget()
        tab_red.setStyleSheet("background-color: red;")
        self.tabs.addTab(tab_red, "roig")

         # Añadimos el QTabWidget al layout principal
        ventana_colores.addWidget(self.tabs)

        # Asignamos el layout a la ventana
        self.setLayout(ventana_colores)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())



        


