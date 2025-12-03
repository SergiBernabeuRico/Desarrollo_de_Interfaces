from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QVBoxLayout,
    QDialog, QDialogButtonBox, QHBoxLayout,
    QColorDialog, QFontDialog
)
from PySide6.QtGui import QAction, QIcon, QFont, QColor
from PySide6.QtCore import Qt
from pathlib import Path
import sys


# ---------------------------------------------------------
# Función para rutas absolutas de imágenes
# ---------------------------------------------------------
def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


# ---------------------------------------------------------
# DIÁLOGO DE PREFERENCIAS (QDialog personalizado)
# ---------------------------------------------------------
class DialogoPreferencias(QDialog):
    """
    Diálogo que permite elegir color de fondo y fuente,
    con una etiqueta de previsualización.
    """

    def __init__(self, color_inicial, fuente_inicial, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Preferencias")

        # Color y fuente actuales del diálogo
        self.color = color_inicial
        self.fuente = fuente_inicial

        # Etiqueta de previsualización
        self.label_preview = QLabel("Hola, usuari!")
        self.label_preview.setAlignment(Qt.AlignCenter)

        # Botón para elegir color
        self.boton_color = QPushButton("Elegir color...")

        # Botón para elegir fuente
        self.boton_fuente = QPushButton("Elegir fuente...")

        # Botonera OK / Cancel
        self.botones = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        # Conexiones
        self.boton_color.clicked.connect(self.seleccionar_color)
        self.boton_fuente.clicked.connect(self.seleccionar_fuente)
        self.botones.accepted.connect(self.accept)
        self.botones.rejected.connect(self.reject)

        # Layouts
        layout_principal = QVBoxLayout()
        fila_botones = QHBoxLayout()
        fila_botones.addWidget(self.boton_color)
        fila_botones.addWidget(self.boton_fuente)

        layout_principal.addWidget(self.label_preview)
        layout_principal.addLayout(fila_botones)
        layout_principal.addWidget(self.botones)

        self.setLayout(layout_principal)

        # Aplicamos estilo inicial a la previsualización
        self.actualizar_preview()

    def seleccionar_color(self):
        nuevo_color = QColorDialog.getColor(self.color, self)
        if nuevo_color.isValid():
            self.color = nuevo_color
            self.actualizar_preview()

    def seleccionar_fuente(self):
        ok, nueva_fuente = QFontDialog.getFont(self.fuente, self)
        if ok:
            self.fuente = nueva_fuente
            self.actualizar_preview()

    def actualizar_preview(self):
        self.label_preview.setFont(self.fuente)
        self.label_preview.setStyleSheet(
            f"background-color: {self.color.name()}"
        )


# ---------------------------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------------------------
class MainWindow(QMainWindow):
    """
    Ventana principal:
    - Menú Configuración -> Preferencias (Ctrl+P) con icono.
    - Botón "Preferencias..." con el mismo icono.
    - Al aceptar el diálogo, aplica color y fuente a la etiqueta central.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Preferencias de Usuario")
        self.resize(500, 300)

        # Color y fuente actuales (por defecto)
        self.color_actual = QColor("white")
        self.fuente_actual = QFont()

        self.crear_centro()
        self.crear_menus()

    # ----------------- Contenido central -----------------
    def crear_centro(self):
        central = QWidget()
        layout = QVBoxLayout()

        # Etiqueta principal
        self.label_saludo = QLabel("Hola, usuari!")
        self.label_saludo.setAlignment(Qt.AlignCenter)
        self.aplicar_estilo_label()

        # Botón "Preferencias..." con icono
        self.boton_preferencias = QPushButton("Preferencias...")
        self.boton_preferencias.setIcon(QIcon(absPath("preferencias.png")))
        self.boton_preferencias.clicked.connect(self.abrir_preferencias)

        layout.addWidget(self.label_saludo)
        layout.addWidget(self.boton_preferencias)

        central.setLayout(layout)
        self.setCentralWidget(central)

    # ----------------- Menú Configuración -----------------
    def crear_menus(self):
        barra_menu = self.menuBar()

        menu_config = barra_menu.addMenu("Configuración")

        # Acción Preferencias con icono e atajo Ctrl+P
        accion_preferencias = QAction(
            QIcon(absPath("preferencias.png")),  # icono
            "Preferencias",
            self
        )
        accion_preferencias.setShortcut("Ctrl+P")
        accion_preferencias.triggered.connect(self.abrir_preferencias)

        menu_config.addAction(accion_preferencias)

    # ----------------- Abrir diálogo -----------------
    def abrir_preferencias(self):
        dialogo = DialogoPreferencias(
            self.color_actual,
            self.fuente_actual,
            self
        )

        if dialogo.exec():  # OK
            self.color_actual = dialogo.color
            self.fuente_actual = dialogo.fuente
            self.aplicar_estilo_label()

    def aplicar_estilo_label(self):
        self.label_saludo.setFont(self.fuente_actual)
        self.label_saludo.setStyleSheet(
            f"background-color: {self.color_actual.name()}"
        )


# ---------------------------------------------------------
# Punto de entrada
# ---------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
