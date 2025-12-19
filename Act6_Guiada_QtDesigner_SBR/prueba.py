from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from primerintento import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    # Heredamos de QMainWindow y de la interfaz
    def __init__(self):
        # Llamamos al constructor explícito de QMainWindow
        super().__init__()


        # Ejecutamos el método setupUi heredado del diseño,
        # gracias al cual se generará la interfaz gráfica
        self.setupUi(self)

        # Configuramos una señal para el botón
        self.pushButton.clicked.connect(self.mostrar_mensaje)

        # Configuramos la señal para salir del programa
        self.actionSalir.triggered.connect(self.close)

    def mostrar_mensaje(self):
        QMessageBox.information(self, "Diálogo", f"El contenido del campo de texto es:\n\n{self.lineEdit.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())