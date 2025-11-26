from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog 
import sys

class MainWindow(QMainWindow):
    # Ventana principal de la aplicación.
    # Hereda de QMainWindow
    # Dentro crearemos un botón que abrirá el selector de color.
    def __init__(self):
        # Llamamos al constructor de QMainWindow
        super().__init__()

        # Ponemos un título a la ventana
        self.setWindowTitle("Aplicación con diálogos")

        # Ajustamos un tamaño inicial a la ventana
        self.resize(480, 320)

        # --- CREACIÓN DEL BOTÓN PRINCIPAL ---
        # Conectamos la señal 'clicked' del botón con un método nuestro.
        # Cuando se pulse el botón, se ejecutará self.mostrar_selector_color.
        self.boton_color = QPushButton("Elige un color")
        self.boton_color.clicked.connect(self.mostrar_selector_color)

        # Colocamos el botón como widget central de la ventana principal.
        self.setCentralWidget(self.boton_color)

    # --- MÉTODO QUE ABRE EL DIÁLOGO DE SELECCIÓN DE COLOR ---
    def mostrar_selector_color(self):
        # Abre un QColorDialog para que el usuario elija un color.
        # Usamos QColorDialog.getColor(), que muestra el diálogo de color y
        # devuelve un objeto QColor con el color elegido.

         # Mostramos el diálogo de selección de color.
        color = QColorDialog.getColor()

        # Es importante comprobar si el usuario ha elegido un color válido.
        # Si cierra el diálogo con "Cancelar", el color NO es válido.
        if color.isValid():
            color_hex = color.name()
            self.boton_color.setStyleSheet(f"background-color: {color_hex}")
            self.setStyleSheet(f"background-color: {color_hex}")

# Punto de entrada del programa (igual que en los ejemplos del profesor)
if __name__ == "__main__":
    # Creamos el objeto QApplication, necesario en todas las aplicaciones Qt.
    app = QApplication(sys.argv)

    # Creamos nuestra ventana principal
    window = MainWindow()

    # Mostramos la ventana
    window.show()

    # Iniciamos el bucle de eventos de la aplicación.
    # Cuando se cierre la ventana, el programa termina
    sys.exit(app.exec())