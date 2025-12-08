"""
Actividad 5 - UD2
Gestor de contactos con PySide6.
"""
from PySide6.QtWidgets import (QApplication,QMainWindow, QListWidget, 
                            QStatusBar, QToolBar, QDockWidget, QLabel,
                            QMessageBox, QInputDialog, QDialog,
                            QFormLayout, QLineEdit, QDialogButtonBox,
)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from pathlib import Path

import sys

def absPath(file_name):
    """Devuelve la ruta absoluta de un archivo en la misma carpeta que este .py."""
    return str(Path(__file__).parent.absolute() / file_name)


class ContactoDialogo(QDialog):
    """Diálogo para introducir un nuevo contacto."""

    def __init__(self):
        # Llamamos al constructor de QDialog
        super().__init__()

        self.setWindowTitle("Nuevo contacto")

        self.campo_nombre = QLineEdit()
        self.campo_telefono = QLineEdit()
        self.campo_email = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Nombre:", self.campo_nombre)
        layout.addRow("Teléfono:", self.campo_telefono)
        layout.addRow("Email:", self.campo_email)

        botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        botones.accepted.connect(self.validar_y_aceptar)
        botones.rejected.connect(self.reject)

        layout.addWidget(botones)
        self.setLayout(layout)

    def validar_y_aceptar(self):
        """Comprueba los datos y acepta el diálogo si son correctos."""
        nombre = self.campo_nombre.text().strip()
        telefono = self.campo_telefono.text().strip()
        email = self.campo_email.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error de datos", "El nombre no puede estar vacío.")
            return

        if not email or ("@" not in email) or ("." not in email):
            QMessageBox.warning(self, "Error de datos", "El email no es válido.")
            return

        self.accept()

    def obtener_datos(self):
        """Devuelve (nombre, teléfono, email)."""
        return (
            self.campo_nombre.text().strip(),
            self.campo_telefono.text().strip(),
            self.campo_email.text().strip(),
        )


class MainWindow(QMainWindow):
    """Ventana principal del gestor de contactos."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Actividad 5 - Gestor de contactos")

        self.contactos = []
        self.siguiente_id = 1

        self.crear_visor()
        self.crear_status_bar()
        self.crear_menu()
        self.crear_toolbar()
        self.crear_dock()
        self.cargar_estilos("estilos.qss")
        self.actualizar_status_bar()

    def crear_visor(self):
        """Crea el visor central con un QListWidget."""
        self.lista_contactos = QListWidget()
        self.setCentralWidget(self.lista_contactos)

    def crear_status_bar(self):
        """Crea la barra de estado."""
        barra_estado = QStatusBar()
        self.setStatusBar(barra_estado)

    def crear_menu(self):
        """Crea la barra de menús y sus acciones."""
        barra_menu = self.menuBar()

        menu_fichero = barra_menu.addMenu("Fichero")
        menu_contactos = barra_menu.addMenu("Contactos")
        menu_ayuda = barra_menu.addMenu("Ayuda")

        self.accion_salir = QAction("Salir", self)
        self.accion_salir.triggered.connect(self.close)

        self.accion_aniadir = QAction("Añadir", self)
        self.accion_aniadir.setShortcut("Ctrl+A")
        self.accion_aniadir.triggered.connect(self.aniadir_contacto)

        self.accion_eliminar = QAction("Eliminar", self)
        self.accion_eliminar.setShortcut("Ctrl+E")
        self.accion_eliminar.triggered.connect(self.eliminar_contacto)

        self.accion_info = QAction("Información", self)
        self.accion_info.triggered.connect(self.mostrar_informacion)

        menu_fichero.addAction(self.accion_salir)
        menu_contactos.addAction(self.accion_aniadir)
        menu_contactos.addAction(self.accion_eliminar)
        menu_ayuda.addAction(self.accion_info)

    def crear_toolbar(self):
        """Crea la barra de herramientas."""
        toolbar = QToolBar("Barra de herramientas")
        self.addToolBar(toolbar)
        toolbar.addAction(self.accion_aniadir)
        toolbar.addAction(self.accion_eliminar)
        toolbar.addSeparator()
        toolbar.addAction(self.accion_salir)

    def crear_dock(self):
        """Crea el dock lateral para la última acción."""
        self.dock = QDockWidget("Última acción", self)
        self.etiqueta_dock = QLabel("Todavía no se ha realizado ninguna acción.")
        self.etiqueta_dock.setWordWrap(True)
        self.dock.setWidget(self.etiqueta_dock)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

    def cargar_estilos(self, nombre_fichero_qss):
        """Carga la hoja de estilos estilos.qss si existe."""
        ruta = absPath(nombre_fichero_qss)
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                estilos = f.read()
                self.setStyleSheet(estilos)
        except Exception as e:
            print("No se pudo cargar la hoja de estilos:", ruta)
            print("Detalle del error:", e)

    def actualizar_status_bar(self):
        """Muestra el número de contactos en la barra de estado."""
        numero = len(self.contactos)
        self.statusBar().showMessage(f"Número de contactos: {numero}")

    def actualizar_visor(self):
        """Actualiza el QListWidget con los contactos actuales."""
        self.lista_contactos.clear()
        for contacto in self.contactos:
            texto = (
                f"ID: {contacto['id']} | "
                f"Nombre: {contacto['nombre']} | "
                f"Teléfono: {contacto['telefono']} | "
                f"Email: {contacto['email']}"
            )
            self.lista_contactos.addItem(texto)

    def actualizar_dock(self, accion, contacto):
        """Muestra en el dock la última acción y el contacto afectado."""
        texto = (
            f"Acción: {accion}\n\n"
            f"ID: {contacto['id']}\n"
            f"Nombre: {contacto['nombre']}\n"
            f"Teléfono: {contacto['telefono']}\n"
            f"Email: {contacto['email']}"
        )
        self.etiqueta_dock.setText(texto)

    def aniadir_contacto(self):
        """Abre el diálogo de nuevo contacto y lo añade a la lista."""
        dialogo = ContactoDialogo()  # sin parent
        if dialogo.exec():
            nombre, telefono, email = dialogo.obtener_datos()
            contacto = {
                "id": self.siguiente_id,
                "nombre": nombre,
                "telefono": telefono,
                "email": email,
            }
            self.contactos.append(contacto)
            self.siguiente_id += 1
            self._actualizar_visor()
            self._actualizar_status_bar()
            self._actualizar_dock("Añadir", contacto)

    def eliminar_contacto(self):
        """Pide un ID y elimina el contacto correspondiente, si existe."""
        if not self.contactos:
            QMessageBox.warning(self, "Lista vacía", "No hay contactos para eliminar.")
            return

        id_introducido, ok = QInputDialog.getInt(
            self,
            "Eliminar contacto",
            "Introduce el ID a eliminar:",
            1,
            1,
            999999,
            1,
        )
        if not ok:
            return

        contacto_encontrado = None
        for contacto in self.contactos:
            if contacto["id"] == id_introducido:
                contacto_encontrado = contacto
                break

        if contacto_encontrado is None:
            QMessageBox.warning(
                self,
                "ID no encontrado",
                "No existe ningún contacto con ese ID.\nIntroduce un ID correcto.",
            )
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            (
                "¿Seguro que deseas eliminar este contacto?\n\n"
                f"ID: {contacto_encontrado['id']}\n"
                f"Nombre: {contacto_encontrado['nombre']}\n"
                f"Teléfono: {contacto_encontrado['telefono']}\n"
                f"Email: {contacto_encontrado['email']}"
            ),
        )
        if respuesta != QMessageBox.Yes:
            return

        self.contactos.remove(contacto_encontrado)
        self._actualizar_visor()
        self._actualizar_status_bar()
        self._actualizar_dock("Eliminar", contacto_encontrado)

    def mostrar_informacion(self):
        """Muestra un mensaje de información de la aplicación."""
        QMessageBox.information(
            self,
            "Información",
            "Gestor de contactos\n\nActividad 5 - Unidad 2",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
