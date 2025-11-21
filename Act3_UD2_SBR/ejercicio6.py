# Ejercicio 6
# Ventana con un GroupBox que contiene 3 QCheckBox
# Cada vez que el usuario marca o desmarca un checkBox, se imprime por consola cuáles están marcados

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QGroupBox, QCheckBox, QVBoxLayout)

class VentanaCheckBox(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("QGroupBox")
        # Ajustamos tamaño 
        self.resize(300, 200)

        # Crear y organizar la interfaz 
        self.crear_interfaz()

    def crear_interfaz(self):
        # Layout principal de la ventana
        layout_principal = QVBoxLayout()

        # --- Layout que rodea los checkBox ---
        self.group_box = QGroupBox("Exclusive Radio Buttons")

        # Layout interno del GroupBox (vertical)
        layout_group = QVBoxLayout()

        # Creamos los checkbox
        self.chk1 = QCheckBox("Primer checkbox")
        self.chk2 = QCheckBox("Segundo checkbox")
        self.chk3 = QCheckBox("Tercer checkbox")

        # Conectamos el cambio de estado de cada checkbox a un mismo método
        self.chk1.stateChanged.connect(self.imprimir_seleccionados)
        self.chk2.stateChanged.connect(self.imprimir_seleccionados)
        self.chk3.stateChanged.connect(self.imprimir_seleccionados)

        # Añadimos los checkbox al layout del group box
        layout_group.addWidget(self.chk1)
        layout_group.addWidget(self.chk2)
        layout_group.addWidget(self.chk3)

        # Asignamos el layout al group box
        self.group_box.setLayout(layout_group)

        # Añadimos el group box al layout principal
        layout_principal.addWidget(self.group_box)

        # Asignamos el layout principal a la ventana
        self.setLayout(layout_principal)

    def imprimir_seleccionados(self):
        # Metodo  que se ejecuta cada vez que cambia el estado de 
        # cualquiera de los checkbox. Imprime por consola los marcados.
        seleccionados = [] # Creamos lista vacía

        if self.chk1.isChecked():
            seleccionados.append("Primer checkbox")
        if self.chk2.isChecked():
            seleccionados.append("Segundo checkbox")
        if self.chk3.isChecked():
            seleccionados.append("Tercer checkbox")

        # Mostramos el resultado por consola
        if seleccionados:
            print("Marcados:", ", ".join(seleccionados))
        else:
            print("Ningún checkbox marcado")

if __name__ == "__main__":
    app =QApplication(sys.argv)

    ventana = VentanaCheckBox()
    ventana.show()

    sys.exit(app.exec())


