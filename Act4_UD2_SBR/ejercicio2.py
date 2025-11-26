from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton, QFontDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación con diálogos")
        self.resize(400, 350)

        # --- CREACIÓN DEL BOTÓN PRINCIPAL ---
        # Creamos un QPushButton con el texto que se ve en el enunciado
        self.boton_fuente = QPushButton("Haz click para que el diálogo aparezca")

        # Conectamos la señal 'clicked' del botón con nuestro método.
        # Cuando se pulse el botón se ejecutará self.mostrar_selector_fuente.
        self.boton_fuente.clicked.connect(self.mostrar_selector_fuente)

        # Colocamos el botón como widget central de la ventana principal.
        self.setCentralWidget(self.boton_fuente)

    # --- MÉTODO QUE ABRE EL DIÁLOGO DE SELECCIÓN DE FUENTE ---
    def mostrar_selector_fuente(self):
        """
        Abre un QFontDialog para que el usuario elija fuente, estilo y tamaño.

        Usamos QFontDialog.getFont(self), igual que en 15-Dialogo_fuente.py.
        Esta función devuelve dos valores:
        - confirmado (bool): True si el usuario pulsa "Aceptar".
        - fuente (QFont): la fuente seleccionada.
        """

        # Mostramos el diálogo de fuente.
        # Pasamos self como ventana padre.
        fuente, confirmado =  QFontDialog.getFont(self)

        # Solo aplicamos la fuente si el usuario ha pulsado "Aceptar".
        if confirmado:
            # fuente es un objeto QFont que ya incluye:
            #   - familia (Ubuntu, Arial, etc.)
            #   - estilo (normal, negrita, cursiva, ...)
            #   - tamaño en puntos
            #
            # Al aplicar setFont sobre el botón, TODO eso se aplica al texto.
            self.boton_fuente.setFont(fuente)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())





