from PySide6.QtWidgets import(QApplication, QMainWindow, QWidget, 
                              QVBoxLayout, QHBoxLayout, QGridLayout, 
                              QGroupBox, QPushButton, QLineEdit, 
                              QTextEdit, QDialogButtonBox, QLabel)
import sys

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts básicos")
        self.resize(600, 400)

        # Creamos el menú, el área central y la botonera
        self.crear_menu()
        self.crear_contenido()

    # -------------------------------------------------
    # MENÚ: Archivo -> Salir
    # -------------------------------------------------

    def crear_menu(self):
        barra_menu = self.menuBar()
        # Menú principal salir
        menu_archivo = barra_menu.addMenu("Archivo")

        # Acción Salir: al pulsarla, se cierra la aplicación.
        accion_salir = menu_archivo.addAction("Salir")
        accion_salir.setShortcut("Ctrl+S")
        accion_salir.triggered.connect(self.close)

    # -------------------------------------------------
    # CONTENIDO CENTRAL (layouts) + QDialogButtonBox
    # -------------------------------------------------

    def crear_contenido(self):
        # Widget central que colgaremos del QMainWindow
        central = QWidget()
        # Layout vertical principal: apila los grupos y la botonera
        layout_principal = QVBoxLayout()
        # ----- 1) QGroupBox: Layout Horizontal -----
        grupo_horizontal = QGroupBox("Layout Horizontal")
        layout_horizontal = QHBoxLayout()

        boton1 = QPushButton("Botón 1")
        boton2 = QPushButton("Botón 2")
        boton3 = QPushButton("Botón 3")
        boton4 = QPushButton("Botón 4")

        layout_horizontal.addWidget(boton1)
        layout_horizontal.addWidget(boton2)
        layout_horizontal.addWidget(boton3)
        layout_horizontal.addWidget(boton4)

        # Asociamos el layout al groupbox
        grupo_horizontal.setLayout(layout_horizontal)

         # ----- 2) QGroupBox: Layout Grid -----
        grupo_grid = QGroupBox("Layout Grid")
        layout_grid = QGridLayout()

        # Etiquetas de texto para las líneas
        etiqueta_linea1 = QLabel("Línea 1")
        etiqueta_linea2 = QLabel("Línea 2")

        # Campos de línea (QLineEdit) para cada línea
        linea1 = QLineEdit()
        linea2 = QLineEdit()

        # QTextEdit a la derecha, ocupando dos filas
        texto = QTextEdit()
        texto.setPlainText("Esto es un QTextEdit")

        # Colocamos los widgets en el grid:
        # fila, columna (y en el QTextEdit indicamos que ocupe 2 filas)
        layout_grid.addWidget(etiqueta_linea1, 0, 0)
        layout_grid.addWidget(linea1, 0, 1)

        layout_grid.addWidget(etiqueta_linea2, 1, 0)
        layout_grid.addWidget(linea2, 1, 1)

        # QTextEdit: empieza en fila 0, col 2, ocupa 2 filas y 1 columna
        layout_grid.addWidget(texto, 0, 2, 2, 1)

        grupo_grid.setLayout(layout_grid)

        # ----- 3) QDialogButtonBox con OK y Cancel -----
        # Creamos la botonera. No conectamos señales porque
        # el enunciado dice que no hace falta que hagan nada.
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout_principal.addWidget(grupo_horizontal)
        layout_principal.addWidget(grupo_grid)
        layout_principal.addWidget(botones)

        # Asignamos el layout principal al widget central
        central.setLayout(layout_principal)

        # Colgamos este widget central del QMainWindow
        self.setCentralWidget(central)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




