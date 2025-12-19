from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from primerintento import Ui_MainWindow
from segundointento import Ui_Form
import sys

class Subventana(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        # Generamos la interfaz de la subventana
        self.setupUi(self)

        # Señal para cerrar la subventana (esto sí está bien)
        self.pushButton.clicked.connect(self.close)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Configuramos la señal para salir del programa
        self.actionSalir.triggered.connect(self.close)

        self.subventana = Subventana()

        # El botón "Enviar" de la ventana principal abre la subventana
        self.pushButton.clicked.connect(self.mostrar_subventana)

    def mostrar_subventana(self):
        # normalmente es self.subventana.label (minúscula), no Label
        self.subventana.label.setText(self.lineEdit.text())
        self.subventana.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Debes crear la ventana principal, no la subventana
    ventana = MainWindow()
    ventana.show()

    sys.exit(app.exec())
