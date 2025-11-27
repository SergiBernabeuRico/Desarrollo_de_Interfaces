# Importamos las clases necesarias de PySide6.
# Todas ellas aparecen en los ejemplos de la UD2.
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QVBoxLayout, QStatusBar
)
from PySide6.QtGui import QIcon, QPixmap
from pathlib import Path
import sys


# ----------------------------------------------------------------------
# Función auxiliar para obtener rutas absolutas (como en códigos del profe)
# ----------------------------------------------------------------------
def absPath(file):
    """
    Devuelve la ruta absoluta al archivo 'file' tomando como base
    la carpeta donde está este script.

    Ejemplo:
        absPath("patito.png")
    """
    return str(Path(__file__).parent.absolute() / file)


# ----------------------------------------------------------------------
# Clase de la subventana que muestra una imagen (Patito o Pingüino)
# ----------------------------------------------------------------------
class VentanaAnimal(QWidget):
    """
    Ventanita sencilla que muestra la imagen de un animal.
    Hereda de QWidget (igual que en 1.Subventana.py).
    """

    def __init__(self, titulo_ventana, ruta_imagen):
        # Llamamos al constructor de QWidget
        super().__init__()

        # Título de la ventana (Patito / Pingüino)
        self.setWindowTitle(titulo_ventana)

        # Tamaño inicial de la ventana
        self.resize(400, 300)

        # Layout vertical para colocar la etiqueta
        layout = QVBoxLayout()

        # Creamos la etiqueta donde se mostrará la imagen
        etiqueta = QLabel()

        # Cargamos la imagen desde disco usando QPixmap
        # IMPORTANTE: la ruta debe existir (nombre de archivo correcto).
        pixmap = QPixmap(absPath(ruta_imagen))

        # Asignamos el QPixmap a la etiqueta
        etiqueta.setPixmap(pixmap)

        # Hacemos que la imagen se escale con el tamaño de la ventana
        etiqueta.setScaledContents(True)

        # Añadimos la etiqueta al layout
        layout.addWidget(etiqueta)

        # Asignamos el layout a la ventana
        self.setLayout(layout)


# ----------------------------------------------------------------------
# Ventana principal con barra de menú, menú Archivo y submenú
# ----------------------------------------------------------------------
class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación.

    - Barra de menú con un menú "Archivo".
    - Dentro de Archivo:
        - Acción "Salir".
        - Separador.
        - Submenú con "Patito" y "Pingüino".
    """

    def __init__(self):
        super().__init__()

        # Tamaño inicial de la ventana principal
        self.resize(480, 320)

        # Título que aparece en la barra de título
        self.setWindowTitle("3-Ejercicio.py")

        # Construimos el menú
        self.construir_menu()

        # Añadimos una barra de estado (parte inferior)
        self.setStatusBar(QStatusBar(self))

    # ------------------------------------------------------------------
    # Construcción de la barra de menú
    # ------------------------------------------------------------------
    def construir_menu(self):
        """
        Crea la barra de menú, el menú Archivo, la acción Salir
        y el submenú con Patito y Pingüino.
        """

        # Obtenemos la barra de menú
        barra_menu = self.menuBar()

        # Creamos el menú principal "Archivo"
        menu_archivo = barra_menu.addMenu("&Archivo")

        # ---- Acción Salir ----
        # Usamos el icono exit.png (como en los ejemplos del profesor).
        # Cambia el nombre si tu archivo se llama distinto.
        menu_archivo.addAction(
            QIcon(absPath("exit.png")),   # icono
            "Salir",                      # texto
            self.close,                   # función que se ejecuta
            "Ctrl+Q"                      # atajo de teclado
        )

        # ---- Separador ----
        menu_archivo.addSeparator()

        # ---- Submenú con animales ----
        submenu_animales = menu_archivo.addMenu("Submenú")

        # Acción Patito
        # OJO: usa el nombre real del archivo (por ejemplo "patito.png")
        self.accion_patito = submenu_animales.addAction(
            QIcon(absPath("patito.png")),
            "Patito"
        )

        # Acción Pingüino
        self.accion_pinguino = submenu_animales.addAction(
            QIcon(absPath("pinguino.png")),
            "Pingüino"
        )

        # Conectamos las señales triggered de las acciones con los métodos
        self.accion_patito.triggered.connect(self.mostrar_patito)
        self.accion_pinguino.triggered.connect(self.mostrar_pinguino)

    # ------------------------------------------------------------------
    # Métodos que abren las subventanas
    # ------------------------------------------------------------------
    def mostrar_patito(self):
        """
        Crea y muestra una ventana con la imagen del patito.
        Guardamos la referencia en self.ventana_patito para que
        el objeto no sea destruido.
        """
        self.ventana_patito = VentanaAnimal("Patito", "patito.png")
        self.ventana_patito.show()

    def mostrar_pinguino(self):
        """
        Crea y muestra una ventana con la imagen del pingüino.
        """
        self.ventana_pinguino = VentanaAnimal("Pingüino", "pinguino.png")
        self.ventana_pinguino.show()


# ----------------------------------------------------------------------
# Punto de entrada del programa
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Creamos la aplicación Qt
    app = QApplication(sys.argv)

    # Creamos la ventana principal
    window = MainWindow()

    # Mostramos la ventana
    window.show()

    # Iniciamos el bucle de eventos
    sys.exit(app.exec_())



