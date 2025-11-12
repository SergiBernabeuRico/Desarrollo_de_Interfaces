""" Act2_UD2  Ejercicio 2
Descripción:
    - Mostrar un listado con todos los meses del año en un QComboBox.
    - Al seleccionar un mes (p. ej., "abril"), imprimir en consola:
        a) La posición real que ocupa (1 = enero, 4 = abril, etc.).
        b) El texto exacto seleccionado. """

from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox
import sys

class MainWindow(QMainWindow):

    """Ventana principal con un QComboBox de meses.
    Al cambiar la selección, se imprime por consola la posición real (1..12)
    y el texto exacto del mes seleccionado. """
    def __init__(self) -> None:
            #   Iniciamos la superclase para heredar el comportamiento de QMainWindow
        super().__init__()

            #   Titulo de la ventana (para identificar la app)   
        self.setWindowTitle("Act2UD2 Ejercicio 2")

            #   --- Crear el combo de de los 12 meses ---
        self.combo = QComboBox(self)
        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]
        self.combo.addItems(meses)

            #   Lo usamos directamente como widget central (válido en QMainWindow)
        self.setCentralWidget(self.combo)

            #   --- Conexión de señales ---
            #   Señal 1: índice cambiado (int). Útil para obtener la posición real.
        self.combo.currentIndexChanged.connect(self.indice_cambiado)

            #   Señal 2: texto cambiado (str). Útil para mostrar el texto exacto.
        self.combo.currentTextChanged.connect(self.texto_cambiado)

            #   Imprimir el estado inicial al arrancar (por claridad de consola)
        idx_inicial = self.combo.currentIndex()
        txt_inicial = self.combo.currentText()
        print(f"[Inicio] Posición real: {idx_inicial +1} | Mes: {txt_inicial}")

            #   Redimensionamos la ventana para que se vea bien
        self.resize(269,80)

        #   --- Slots ---
    def indice_cambiado(self,idx: int) -> None:
        """Slot llamado cuando cambia el índice del QComboBox.
        Mostramos la posición real (1..12) y también el texto usando el índice recibido."""

            #   Precaución: cuando no hay selección, Qt puede emitir -1; aquí no debería pasar
            #   porque siempre hay meses en combo, pero lo manejamos por seguridad.  
        if idx < 0:
            print("f[Cambio] Posición real: {posicion_real} | Mes: {texto}")
            return
        
            #    La posición real es el índice base 0 + 1
        posicion_real = idx + 1
        texto = self.combo.itemText(idx)
        print(f"[Cambio] Posición real: {posicion_real} | Mes: {texto}")

    def texto_cambiado(self, texto: str) -> None:
        """Slot llamado cuando cambia el texto del QComboBox.
        Muestra el texto exacto seleccionado (útil para confirmar el cambio)."""

        print(f"[Cambio] Texto seleccionado: {texto}")

if __name__ == "__main__":
        #   Punto de entrada estandar de la app
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



