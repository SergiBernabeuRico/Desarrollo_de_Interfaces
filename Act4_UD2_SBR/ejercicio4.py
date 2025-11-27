# ------------------- IMPORTACIONES -------------------
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import sys   # Ya lo usamos en muchos ejemplos de la UD2


# -------- FUNCIÓN AUXILIAR PARA LAS RUTAS (absPath) --------
def absPath(file):
    """
    Devuelve la ruta absoluta del archivo 'file' a partir
    de la carpeta donde está este script.

    Ejemplo:
        absPath("imprimir.png")
    """
    return str(Path(__file__).parent.absolute() / file)


# ----------------- VENTANA PRINCIPAL -----------------
class MainWindow(QMainWindow):
    """
    Ventana principal con:
    - Menú.
    - Barra de herramientas.
    - Barra de estado.

    Y una zona central con algunos textos tipo "Componente base 1".
    """

    def __init__(self):
        super().__init__()

        # Título y tamaño inicial de la ventana
        self.setWindowTitle(
            "Ventana principal con menú, barra de herramientas y barra de estado"
        )
        self.resize(600, 400)

        # Creamos los tres bloques principales
        self.crear_componentes_centrales()
        self.crear_barra_estado()
        self.crear_acciones_y_menus()

    # -------------------------------------------------
    # ZONA CENTRAL (contenido principal)
    # -------------------------------------------------
    def crear_componentes_centrales(self):
        """
        Crea un widget central sencillo con dos etiquetas, para imitar
        la idea de "Componente base 1" y "Componente principal".
        """

        # Widget que será el contenido central
        central = QWidget()

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta superior
        etiqueta_superior = QLabel("Componente base 1")
        # Etiqueta central
        etiqueta_central = QLabel("Componente principal")

        # Añadimos las etiquetas al layout
        layout.addWidget(etiqueta_superior)
        layout.addWidget(etiqueta_central)

        # Asignamos el layout al widget central
        central.setLayout(layout)

        # Establecemos el widget central en el QMainWindow
        self.setCentralWidget(central)

    # -------------------------------------------------
    # BARRA DE ESTADO
    # -------------------------------------------------
    def crear_barra_estado(self):
        """
        Crea la barra de estado y muestra:
        - Un mensaje temporal: "Listo. Esperando acción".
        - Un mensaje permanente con el sistema operativo (Linux, Windows...).
        """

        # Creamos el objeto QStatusBar y lo asignamos a la ventana
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)

        # Mensaje temporal (aparecerá unos segundos en la parte izquierda)
        # El segundo parámetro son milisegundos: 3000 = 3 segundos.
        barra_estado.showMessage("Listo. Esperando acción", 3000)

        # Detectamos el sistema operativo de forma sencilla
        if sys.platform.startswith("linux"):
            nombre_sistema = "Linux"
        elif sys.platform.startswith("win"):
            nombre_sistema = "Windows"
        elif sys.platform.startswith("darwin"):
            nombre_sistema = "macOS"
        else:
            nombre_sistema = sys.platform

        # Creamos una etiqueta con el nombre del sistema y la añadimos
        # como "widget permanente" en la barra de estado (parte derecha).
        etiqueta_sistema = QLabel(nombre_sistema)
        barra_estado.addPermanentWidget(etiqueta_sistema)

    # -------------------------------------------------
    # ACCIONES, MENÚS Y BARRA DE HERRAMIENTAS
    # -------------------------------------------------
    def crear_acciones_y_menus(self):
        """
        Crea la acción principal de la aplicación, la añade:
        - a un submenú del menú principal
        - y a la barra de herramientas

        La acción tiene:
        - icono
        - atajo de teclado Ctrl+I
        - texto de ayuda en la barra de estado
        """

        # ---------- 1) Creamos la ACCIÓN ----------
        # Icono: usa un fichero de imagen del profe (por ejemplo "imprimir.png").
        # Cambia el nombre si el archivo se llama de otra forma.
        icono_imprimir = QIcon(absPath("printer.png"))

        self.accion_imprimir = QAction(icono_imprimir, "Imprimir por consola", self)

        # Atajo de teclado (shortcut) Ctrl+I
        self.accion_imprimir.setShortcut("Ctrl+I")

        # Texto que aparecerá en la barra de estado cuando pasemos el ratón
        self.accion_imprimir.setStatusTip("Imprimir medio consola")

        # Conectamos la acción con el método que hará el trabajo
        self.accion_imprimir.triggered.connect(self.imprimir_por_consola)

        # ---------- 2) Creamos la BARRA DE MENÚ ----------
        barra_menu = self.menuBar()

        # Menú principal (en la captura se ve algo como "Menú")
        menu_principal = barra_menu.addMenu("&Menú")

        # Submenú que contendrá la acción, con icono
        sub_menu = menu_principal.addMenu(icono_imprimir, "Opciones de impresión")

        # Añadimos la acción al submenú
        sub_menu.addAction(self.accion_imprimir)

        # ---------- 3) Creamos la BARRA DE HERRAMIENTAS ----------
        barra_herramientas = QToolBar("Barra de herramientas principal")
        self.addToolBar(barra_herramientas)

        # Añadimos la misma acción a la barra de herramientas.
        # De esta forma, menú, toolbar y atajo de teclado comparten acción.
        barra_herramientas.addAction(self.accion_imprimir)

    # -------------------------------------------------
    # SLOT / MÉTODO que ejecuta la acción
    # -------------------------------------------------
    def imprimir_por_consola(self):
        """
        Método que se ejecuta cuando:
        - se pulsa la opción del submenú,
        - se hace clic en el botón de la barra de herramientas,
        - o se usa el atajo de teclado Ctrl+I.
        """

        print("Acción lanzada a través del menú, uso del atajo de teclado o de la barra de herramientas")


# ----------------- PUNTO DE ENTRADA -----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
