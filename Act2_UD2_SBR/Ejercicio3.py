""" Act2_UD2 Ejercicio 3
Descripción (según enunciado):
    - La ventana dispone de un botón.
    - Cada vez que se hace clic, se muestra un refrán aleatorio en el **título de la ventana**.
    - Si el refrán es "De los errores se aprende", el botón queda **deshabilitado**.
    - Usaremos `choice` de la librería estándar `random`."""

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice
import sys


class MainWindow(QMainWindow):
    """Ventana principal con un botón que muestra refranes aleatorios en el título.
    Si el refrán obtenido es "De los errores se aprende", el botón se desactiva
    para impedir más clics."""

    def __init__(self) -> None:
        super().__init__()

            #   Título inicial de la ventana
        self.setWindowTitle("Act2_UD2 Ejercicio 3")

            #   Lista de refranes (exactamente los proporcionados en el enunciado)
        self.refranes = [
            "Haz el bien sin mirar a quien",
            "Más vale prevenir que curar",
            "A mal tiempo, buena cara",
            "Quien tiene un amigo tiene un tesoro",
            "La avaricia rompe el saco",
            "De los errores se aprende",
        ]

            #   Creamos un botón simple y lo usamos como widget central
        self.boton = QPushButton("Mostrar refrán", self)
        self.setCentralWidget(self.boton)

            #   Conectamos la señal de clic del botón a nuestro slot/manejador
        self.boton.clicked.connect(self.mostrar_refran)

            #   Ajustamos un tamaño cómodo de ventana (opcional)
        self.resize(320, 120)

    def mostrar_refran(self) -> None:
        """Elige un refrán aleatorio y lo coloca en el título de la ventana.
        Si el refrán es "De los errores se aprende", se deshabilita el botón
        para evitar más clics."""

        refran = choice(self.refranes)  # elegimos uno al azar

            #   Mostramos el refrán elegido en el título de la ventana (QMainWindow)
        self.setWindowTitle(refran)

            #   Si es el refrán "detonante", deshabilitamos el botón
        if refran == "De los errores se aprende":
            self.boton.setEnabled(False)


if __name__ == "__main__":
        #   Punto de entrada estándar de una app Qt/PySide6
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
