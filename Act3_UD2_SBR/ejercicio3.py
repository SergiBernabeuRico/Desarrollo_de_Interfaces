# Ejercicio 3
# Ventana de tipo formulario con QLineEdit, QSpinBox y QDuobleSpinBox

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QLineEdit, QSpinBox, QDoubleSpinBox, QFormLayout)

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de la ventana
        self.setWindowTitle("Formulari")
        # Damos tamaño a la ventana
        self.resize(400, 300)

        # Crear y organizar los widgets
        self.crear_interfaz()

    def crear_interfaz(self):
        # Layout en forma de formulario (etiqueta + campo por fila)
        layoutFormulario = QFormLayout()

        # --- Campo de texto ---
        self.campo_texto = QLineEdit()
        # Añadimos fila: etiqueta "Text: " y el QLineEdit
        layoutFormulario.addRow("Text:", self.campo_texto)

        # --- Campo entero (QSpinBox) ---
        self.campo_entero = QSpinBox()
        # Configuración del QSpinBox: límites y valor inicial
        self.campo_entero.setRange(0, 100)      # mínimo 0, máximo 100
        self.campo_entero.setValue(0)              # valor inicial 0
        # Añadimos fila: etiqueta "Entrada: " y el QSpinBox
        layoutFormulario.addRow("Entrada: ", self.campo_entero)

        # --- Campo decimal ---
        self.campo_decimal = QDoubleSpinBox()
        # Configuramos el número de decimales, el rango, el incremento y el valor inicial
        self.campo_decimal.setDecimals(2)               # dos decimales
        self.campo_decimal.setRange(0.00, 100.00)       # rango de 0 a 100
        self.campo_decimal.setSingleStep(0.10)          # incremento de 0.10 cada vez que se pulsa las flechas
        self.campo_decimal.setValue(0)                   # valor inicial 0
        # Añadimos fila: etiqueta "Decimal: " y el QDoubleSpinBox
        layoutFormulario.addRow("Decimal: ", self.campo_decimal)

        # Asignamos el layout de formulario a la ventana
        self.setLayout(layoutFormulario)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaFormulario()
    ventana.show()

    sys.exit(app.exec())

