""" Act2_UD2 Ejercicio 1
Descripción:
    - Crear una ventana con un QLineEdit (caja de texto) y un QLabel (etiqueta).
    - El QLineEdit debe aceptar como máximo 5 caracteres y tener tamaño fijo 50x30 px.
    - El QLabel debe tener tamaño 50x30 px y estar desplazado 50 px para no solaparse con el QLineEdit (es decir, colocado justo a la derecha).
    - Cada vez que cambie el texto del QLineEdit, el QLabel mostrará ese mismo texto. """

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    """ Ventana principal de la aplicación.
    Hereda de QMainWindow para disponer de una ventana con barra de título y área central 
    donde colocaremos un widget contenedor con nuestros componentes (QLineEdit y QLabel)."""

    def __init__(self) -> None:
            #   Iniciamos la superclase para heredar el comportamiento de QMainWindow
        super().__init__()

            #   Titulo de la ventana (para identificar la app)
        self.setWindowTitle("Act2_UD2 Ejercicio 1")

            #   Creamos un widget contenedor simple (QWidget) que hará de área central
        contenedor = QWidget(self)
        self.setCentralWidget(contenedor)

            #   --- Creación de componentes ---
            #   1) QlineEdit: caja de texto editable
        self.caja = QLineEdit(contenedor)

            #   Fijamos el tamaño a 50x30 píxeles
        self.caja.setFixedSize(50, 30)

            #   Máximo de caracteres permitido: 5
        self.caja.setMaxLength(5)

            #   Posicionamos la caja dentro del contenedor usando coordenadas (x, y)
            #   La situamos a 10 px del borde izquierdo y 10 px del borde superior
        self.caja.move(10, 10)


            #   2) Qlabel: Etiqueta que reflejará el texteo de la caja
        self.etiqueta = QLabel(contenedor)

            #   Fijamos el mismo tamaño 50x30
        self.etiqueta.setFixedSize(50, 30)

            #   Alineamos el texto en el centro para que se vea mejor
        self.etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            #   "Desplazamos 50 px para no solaparse" con el QLineEdit. Como la caja mide
            #   50 px de ancho, colocar la etiqueta a +50 px en X la ubicará justo a la derecha.
            #   Además, añadimos un pequeño margen (10 px) desde el borde izquierdo donde
            #   está la caja, que comienza en x=10, por lo que:
            #       x_etiqueta = x_caja + ancho_caja + separación
            #                  = 10 + 50 + 0 -> si seguimos literalmente "desplazar 50 px"
            #   Para que quede claro en pantalla, puedes añadir 10 px extra si lo prefieres.
        self.etiqueta.move(10 + 50, 10) # cumple el desplazamiento de 50px

            # --- Conexión de señal a slot ---
            #   Cada vez que cambie el texto de la caja, actualizamos el texto de la etiqueta.
            #   QLineEdit emite la señal textChanged(str) con el nuevo contenido.
        self.caja.textChanged.connect(self.actualizar_etiqueta)

            #   Ajuste de tamaño de la ventana
            #   Redimensionamos la ventana para que quepan ambos widgets
            #   y un margen alrededor de 200x60
        self.resize(200, 60)


            # --- Slots (manejadores) ---
    def actualizar_etiqueta(self, texto:str) -> None:

        """ Slot que acctualiza el contenideo del Qlabel con el texto recibido
        Parámetros:
            texto(str): el texto actual del QLineEdit emitido por la señal textChanged. """
        
        self.etiqueta.setText(texto)


if __name__ == "__main__":
        #   Punto de entrada estándar de una app Qt/PySide6.
    app = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
    

            

        


