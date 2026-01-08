"""
Gestor de contactos - PySide6
"""
import sys  # Necesario para QApplication y el bucle de eventos
from pathlib import Path  # Para rutas absolutas

# Widgets principales 
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QStatusBar, QToolBar, QDockWidget,
    QLabel, QMessageBox, QInputDialog, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
)
from PySide6.QtGui import (QAction, QIcon)  # Acciones reutilizables en menú/toolbar
from PySide6.QtCore import Qt  # Para ubicar el dock


def absPath(file_name: str) -> str:
    """Devuelve la ruta absoluta a un archivo en la misma carpeta que este .py."""
    return str(Path(__file__).parent.absolute() / file_name)


class DialogoContacto(QDialog):
    """Diálogo sencillo para pedir nombre, teléfono y email"""

    def __init__(self, parent=None):
        super().__init__(parent)  # Importante: parent para que el diálogo sea modal respecto a la ventana
        self.setWindowTitle("Nuevo contacto")  # Título del diálogo

        # Campos de texto (QLineEdit)
        self.txt_nombre = QLineEdit()
        self.txt_telefono = QLineEdit()
        self.txt_email = QLineEdit()

        # Layout de formulario: etiqueta + campo 
        layout = QFormLayout()
        layout.addRow("Nombre:", self.txt_nombre)
        layout.addRow("Teléfono:", self.txt_telefono)
        layout.addRow("Email:", self.txt_email)

        # Botones estándar OK/Cancel (QDialogButtonBox)
        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.button(QDialogButtonBox.Ok).setText("Aceptar")       # Personalizamos texto
        botones.button(QDialogButtonBox.Cancel).setText("Cancelar")  # Personalizamos texto 

        # Conectamos señales: validamos antes de aceptar; cancelar cierra directamente
        botones.accepted.connect(self.validar_y_aceptar)
        botones.rejected.connect(self.reject)

        # Añadimos botones y aplicamos layout
        layout.addRow(botones)
        self.setLayout(layout)

    def validar_y_aceptar(self):
        # Leemos y limpiamos espacios (strip) para evitar entradas vacías por espacios
        nombre = self.txt_nombre.text().strip()
        email = self.txt_email.text().strip()

        # Validación mínima del nombre: no puede quedar vacío
        if nombre == "":
            QMessageBox.warning(self, "Datos incorrectos", "El nombre no puede estar vacío.")
            return

        # Validación mínima del email: contiene @ y .
        if ("@" not in email) or ("." not in email):
            QMessageBox.warning(self, "Datos incorrectos", "El email no parece válido.")
            return

        # Si todo está bien, aceptamos el diálogo (devuelve QDialog.Accepted)
        self.accept()

    def datos(self):
        """Devuelve una tupla (nombre, telefono, email)."""
        # Centralizamos aquí la lectura para que la ventana principal lo tenga fácil
        return (
            self.txt_nombre.text().strip(),
            self.txt_telefono.text().strip(),
            self.txt_email.text().strip(),
        )


class MainWindow(QMainWindow):
    """Ventana principal del gestor de contactos."""

    def __init__(self):
        super().__init__()  # Inicializa QMainWindow
        self.setWindowTitle("Gestor de contactos")  # Título de ventana

        # Estructura de datos simple en memoria: lista de diccionarios
        self.contactos = []
        self.siguiente_id = 1  # Generador de IDs incremental

        # Construimos UI por partes
        self.construir_visor()
        self.construir_barra_estado()
        self.construir_menu()
        self.construir_toolbar()
        self.construir_dock()

        # Cargamos estilos opcionales (como en el apartado de QSS del ZIP)
        self.cargar_qss()

        # Al iniciar, actualizamos estado y lista
        self.actualizar_lista()
        self.actualizar_estado()

    def construir_visor(self):
        """Crea el QListWidget central para visualizar contactos."""
        # ListWidget: lista como widget central
        self.lista = QListWidget()
        self.setCentralWidget(self.lista)

    def construir_barra_estado(self):
        """Crea la barra de estado (status bar)."""
        # QStatusBar y setStatusBar
        self.setStatusBar(QStatusBar(self))

    def construir_menu(self):
        """Crea la barra de menús con acciones reutilizables."""
        # Recuperamos la barra de menú
        menu = self.menuBar()

        # Creamos menús principales
        menu_fichero = menu.addMenu("Fichero")
        menu_contactos = menu.addMenu("Contactos")
        menu_ayuda = menu.addMenu("Ayuda")

        # Acción SALIR (reutilizable también en toolbar)
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut("Ctrl+Q")  # Atajo típico
        self.accion_salir.triggered.connect(self.close)

        # Acción AÑADIR (abre diálogo y añade a la lista)
        self.accion_añadir = QAction("Añadir", self)
        self.accion_añadir.setShortcut("Ctrl+A")
        self.accion_añadir.triggered.connect(self.aniadir_contacto)

        # Acción ELIMINAR (pide ID y elimina)
        self.accion_eliminar = QAction("Eliminar", self)
        self.accion_eliminar.setShortcut("Ctrl+E")
        self.accion_eliminar.triggered.connect(self.eliminar_contacto)

        # Acción INFO (mensaje simple)
        self.accion_info = QAction("Información", self)
        self.accion_info.setShortcut("Ctrl+I")
        self.accion_info.triggered.connect(self.mostrar_info)
        icono_info = "info.png"
        self.accion_info.setIcon(QIcon(absPath(icono_info)))

        # Añadimos acciones a sus menús
        menu_fichero.addAction(self.accion_salir)
        menu_contactos.addAction(self.accion_añadir)
        menu_contactos.addAction(self.accion_eliminar)
        menu_ayuda.addAction(self.accion_info)

    def construir_toolbar(self):
        """Crea la barra de herramientas usando las mismas acciones del menú."""
        # Igual que en los ejemplos
        toolbar = QToolBar("Herramientas")
        self.addToolBar(toolbar)

        # Creamos variables con el nombre de las imagenes que vamos a utilizar
        icono_añadir = "anadir.png"
        icono_eliminar = "eliminar.png"
        icono_salir = "exit.png"
        

        # setIcon define la imagen que se verá en el botón del toolbar
        self.accion_añadir.setIcon(QIcon(absPath(icono_añadir)))
        self.accion_eliminar.setIcon(QIcon(absPath(icono_eliminar)))
        self.accion_salir.setIcon(QIcon(absPath(icono_salir)))
        

        # Definimos una descripción que aparecerá al pasar el ratón por encima del botón
        self.accion_añadir.setToolTip("Añadir contacto")
        self.accion_eliminar.setToolTip("Eliminar contacto")
        self.accion_salir.setToolTip("Clicar para salir")

        # Reutilizamos acciones (así no duplicamos lógica)
        toolbar.addAction(self.accion_añadir)
        toolbar.addAction(self.accion_eliminar)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_salir)

    def construir_dock(self):
        """Crea el dock lateral de 'Última acción'."""
        # QDockWidget + setWidget + addDockWidget
        self.dock = QDockWidget("Última acción", self)

        # Etiqueta para escribir el texto (wordwrap para que no se salga)
        self.lbl_dock = QLabel("Todavía no se ha realizado ninguna acción.")
        self.lbl_dock.setWordWrap(True)

        # Asignamos el widget al dock y lo colocamos a la derecha
        self.dock.setWidget(self.lbl_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def cargar_qss(self):
        """Carga estilos.qss (en la misma carpeta que el .py) y lo aplica."""
        # se usa absPath + open + setStyleSheet
        ruta = absPath("estilos.qss")

        # Intentamos abrir el fichero y aplicar el contenido como hoja de estilos
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())
        except:
            # Si falla, lo avisamos por consola (como en el ejemplo)
            print("Error abriendo estilos", ruta)


    def actualizar_estado(self):
        """Actualiza la barra de estado con el número de contactos."""
        # Estado = len(lista). Mensaje simple y claro
        self.statusBar().showMessage(f"Número de contactos: {len(self.contactos)}")

    def actualizar_lista(self):
        # Vuelca self.contactos en el QListWidget
        self.lista.clear()

        # Convertimos cada contacto a una línea de texto legible
        for c in self.contactos:
            linea = f"ID {c['id']} | {c['nombre']} | {c['telefono']} | {c['email']}"
            self.lista.addItem(linea)

    def actualizar_dock(self, accion: str, contacto: dict):
        """Muestra en el dock qué ha pasado y con qué contacto."""
        # Texto multilínea (dock) como en tu aplicación original
        texto = (
            f"Acción: {accion}\n\n"
            f"ID: {contacto['id']}\n"
            f"Nombre: {contacto['nombre']}\n"
            f"Teléfono: {contacto['telefono']}\n"
            f"Email: {contacto['email']}"
        )
        self.lbl_dock.setText(texto)

    def aniadir_contacto(self):
        """Abre el diálogo y añade un contacto si se acepta."""
        # Diálogo propio
        dialogo = DialogoContacto(self)

        # exec() bloquea hasta Aceptar/Cancelar (estilo estándar Qt)
        if dialogo.exec():
            nombre, telefono, email = dialogo.datos()

            # Creamos dict simple 
            contacto = {
                "id": self.siguiente_id,
                "nombre": nombre,
                "telefono": telefono,
                "email": email,
            }

            # Guardamos en memoria y avanzamos el ID
            self.contactos.append(contacto)
            self.siguiente_id += 1

            # Refrescamos vista + estado + dock
            self.actualizar_lista()
            self.actualizar_estado()
            self.actualizar_dock("Añadir", contacto)

    def eliminar_contacto(self):
        """Pide un ID y elimina si existe (con confirmación)."""
        # Si no hay contactos, avisamos y salimos
        if len(self.contactos) == 0:
            QMessageBox.warning(self, "Lista vacía", "No hay contactos para eliminar.")
            return

        # Pedimos un entero
        id_borrar, ok = QInputDialog.getInt(
            self,
            "Eliminar contacto",
            "Introduce el ID a eliminar:",
            1,   # valor por defecto
            1,   # mínimo
            999999,  # máximo
            1    # paso
        )

        # Si el usuario cancela, no hacemos nada
        if not ok:
            return

        # Buscamos el contacto con ese ID (búsqueda lineal)
        encontrado = None
        for c in self.contactos:
            if c["id"] == id_borrar:
                encontrado = c
                break

        # Si no existe, avisamos
        if encontrado is None:
            QMessageBox.warning(self, "ID no encontrado", "No existe ningún contacto con ese ID.")
            return

        # Confirmación antes de borrar (evita errores)
        resp = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Eliminar este contacto?\n\nID: {encontrado['id']}\nNombre: {encontrado['nombre']}"
        )

        # Si no se confirma, salimos
        if resp != QMessageBox.Yes:
            return

        # Eliminamos de la lista en memoria
        self.contactos.remove(encontrado)

        # Refrescamos UI
        self.actualizar_lista()
        self.actualizar_estado()
        self.actualizar_dock("Eliminar", encontrado)

    def mostrar_info(self):
        """Muestra un cuadro de información sencillo."""
        QMessageBox.information(
            self,
            "Información",
            "Gestor de contactos\n\n(menús, docks, diálogos, QSS)."
        )

if __name__ == "__main__":
    # Punto de entrada típico de Qt: QApplication -> ventana -> show -> exec()
    app = QApplication(sys.argv)

    # Creamos y mostramos la ventana principal
    window = MainWindow()
    window.resize(700, 400)  # Tamaño inicial cómodo
    window.show()

    # Arrancamos el bucle principal de eventos
    sys.exit(app.exec())
