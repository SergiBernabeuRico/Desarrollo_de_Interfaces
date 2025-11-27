from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QHBoxLayout, QVBoxLayout, QGroupBox, 
                               QPushButton)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Botones alternantes")
        self.resize(400,200)
        self.crear_contenido()

    def crear_contenido(self):
        central = QWidget()
        layout_principal = QVBoxLayout()
        grupo_horizontal = QGroupBox("Layout Horizontal")
        layout_horizontal = QHBoxLayout()

        # Lista donde guardaremos los botones
        # útil para usarlos todos a la vez
        self.botones = []

    # --------- CREACIÓN DE LOS 4 BOTONES CON UN BUCLE FOR ---------
        for i in range(4):
            boton = QPushButton()   # Crea un botón sin texto
            boton.setCheckable(True)    # Botón alternante

            # Color inicial verde (estado no "no pulsado")
            boton.setStyleSheet("Background-color: green")

            # Conectamos la señal clicked a nuestro método cambiar_color
            boton.clicked.connect(self.cambiar_color)

            # Hacerlos un poco más anchos y altos
            boton.setFixedSize(60,25)

            # Añadimos el botón al layout_horizontal y la lista
            layout_horizontal.addWidget(boton)
            self.botones.append(boton)

        # Asociamos el layout_horizontal al GroupBox
        grupo_horizontal.setLayout(layout_horizontal)

        # Añadimos al GroupBox al layout_principal
        layout_principal.addWidget(grupo_horizontal)

        # Asignamos el grupo_horizontal al widget central
        central.setLayout(layout_principal)

        #Establecemos el widget central a la ventana principal
        self.setCentralWidget(central)

    # ------------------------------------------------------------------
    # SLOT: cambia el color del botón que se ha pulsado
    # ------------------------------------------------------------------
    def cambiar_color(self):
        sender = self.sender()

        # Si está clicado, lo ponemos en rojo, si no, en verde
        if sender.isChecked():
            sender.setStyleSheet("background-color: red")
        else:
            sender.setStyleSheet("background-color: green")

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
