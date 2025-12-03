from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QLineEdit, QVBoxLayout, QDockWidget, 
                               QToolBar)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QAction
from pathlib import Path

import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("7-Ejercicio7.py")
        self.resize(700,400)

        # Creamos el área central gris y los docks de colores
        self.crear_centro()
        self.crear_docks()

        # Creamos la barra de menús Archivo, Ayuda, Ver)
        self.crear_menus()

        # Creamos la barra de herramientas con las dos imágenes
        self.crear_toolbar()

    # ---------------------------------------------------------
    # BARRA DE HERRAMIENTAS CON DOS ICONOS
    # ---------------------------------------------------------
    def crear_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        accion_info = QAction(QIcon(absPath("info.png")), "Información", self)
        toolbar.addAction(accion_info)

        accion_cerrar = QAction(QIcon(absPath("exit.png")), "Cerrar aplicación", self)
        accion_cerrar.triggered.connect(self.close)
        toolbar.addAction(accion_cerrar)

        toolbar.setIconSize(QSize(32,32))

        
    # ---------------------------------------------------------
    # CONTENIDO CENTRAL (zona gris)
    # ---------------------------------------------------------
    def crear_centro(self):
        central = QWidget()
        central.setStyleSheet("background-color: gray")
        self.setCentralWidget(central)

    # ---------------------------------------------------------
    # CREACIÓN DE LOS 3 DOCKS
    # ---------------------------------------------------------
    def crear_docks(self):
        # DOCK 1 (blanco de la izquierda)
        self.dock1 = QDockWidget("DOCK 1", self)
        # Contenido del DOCK 1
        contenido_dock1 = QWidget()
        contenido_dock1.setStyleSheet("background-color: white")

        layout_dock1 = QVBoxLayout()
        self.linea_dock1 = QLineEdit()

        layout_dock1.addWidget(self.linea_dock1)
        contenido_dock1.setLayout(layout_dock1)

        # Asignamos el contenido al Dock y añadimos el Dock a la izquierda
        self.dock1.setWidget(contenido_dock1)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)

        # DOCK 2 (amarillo de la derecha)
        self.dock2 = QDockWidget("DOCK 2", self)
        # Contenido del DOCK 2
        contenido_dock2 = QWidget()
        contenido_dock2.setStyleSheet("background-color: yellow")

        # Asignamos el contenido al Dock y añadimos el Dock a la derecha
        self.dock2.setWidget(contenido_dock2)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock2)

        # DOCK 3 (bajo azul)
        self.dock3 = QDockWidget("DOCK 3", self)
        # Contenido del DOCK 3
        contenido_dock3 = QWidget()
        contenido_dock3.setStyleSheet("background-color: blue")

        # Asignamos el contenido al Dock y añadimos el Dock a la parte de bajo
        self.dock3.setWidget(contenido_dock3)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock3)

        contenido_dock3.setMinimumHeight(80)

    # ---------------------------------------------------------
    # MENÚS (Archivo, Ayuda, Ver)
    # ---------------------------------------------------------
    def crear_menus(self):
        barra_menu = self.menuBar()

        # Menú Archivo (vacío en el ejercicio)
        barra_menu.addMenu("Archivo")
        # Menú Ayuda (vacío en el ejercicio)
        barra_menu.addMenu("Ayuda")
        # Menú Ver con la opción de mostrar los 3 docks
        menu_ver = barra_menu.addMenu("Ver")

        # Acción de mostrar DOCK 1
        accion_dock1 = menu_ver.addAction("Mostrar DOCK 1")
        accion_dock1.triggered.connect(self.mostrar_dock1)

        # Acción de mostrar DOCK 2
        accion_dock2 = menu_ver.addAction("Mostrar DOCK 2")
        accion_dock2.triggered.connect(self.mostrar_dock2)

        # Acción de mostrar DOCK 3
        accion_dock3 = menu_ver.addAction("Mostrar DOCK 3")
        accion_dock3.triggered.connect(self.mostrar_dock3)

        
    # ---------------------------------------------------------
    # MÉTODOS PARA MOSTRAR LOS DOCKS DESDE EL MENÚ "Ver"
    # ---------------------------------------------------------
    def mostrar_dock1(self):
        self.dock1.show()
    def mostrar_dock2(self):
        self.dock2.show()
    def mostrar_dock3(self):
        self.dock3.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



        



