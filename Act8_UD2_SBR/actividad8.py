"""
Gestor de contactos - PySide6
"""
import sys  # Necesario para QApplication y el bucle de eventos
import sqlite3 # Librería para la gestión de la base de datos   ---> No la usamos en la ACT8
from pathlib import Path  # Para rutas absolutas

# Widgets principales 
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidget, QStatusBar, QToolBar, QDockWidget,
    QLabel, QMessageBox, QInputDialog, QDialog, QFormLayout, QTableView, QLineEdit, QDialogButtonBox
)
from PySide6.QtGui import (QAction, QIcon)  # Acciones reutilizables en menú/toolbar
from PySide6.QtCore import Qt  # Para ubicar el dock
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlQuery)


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

        # Creamos/Conectamos la base de datos 
        self.conectar_bd()

        # Creamos la tabla si aún no existe
        self.creamos_tabla_si_no_existe() 

        self.configurar_modelo_y_tabla()
        self.conectar_seleccion_de_fila()

        # Función para cargar los contactos en QListWidget y que se muestren al iniciar el programa
        self.cargar_contactos_desde_bd()

        # Al finalizar actualizamos
        self.actualizar_lista()
        self.actualizar_estado()


    # Al realizar la Act8 el QListWidget ha sido sustituído por QTableView
    # (el programa ya no muestra el ListWidget)
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

    def configurar_modelo_y_tabla(self):
        """
        Crea un modelo QSqlTableModel vinculado a la tabla 'contactos'
        y la QTableView para mostrar los datos
        """
        self.modelo = QSqlTableModel(self, self.db)
        self.modelo.setTable("contactos")

        # Estrategia OnFieldChange:
        # cualquier cambio en la celda se guarda directamente en la BD
        self.modelo.setEditStrategy(QSqlTableModel.OnFieldChange)
        
        # Ejecuta una consulta SELECT para cargar los datos de la tabla personasen el modelo
        self.modelo.select()

        # Nombres para las columnas
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombre")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Tlfn")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Email")

        # Creamos la vista de tabla
        self.tabla = QTableView()
        self.tabla.setModel(self.modelo)

        # Ocultar la columna ID (columna 0)
        self.tabla.setColumnHidden(0, True)

        # Ajustar el tamaño de las columnas
        self.tabla.resizeColumnsToContents()

        # Añadimos la tabla al centro
        self.setCentralWidget(self.tabla)

    def conectar_seleccion_de_fila(self):
        """
        Conecta la señal de cambio de fila seleccionada.
        Cuando el usuario selecciona una fila en la tabla,
        leemos sus datos y los mostramos (por consola y en la barra de estado)
        """
        sel_modelo = self.tabla.selectionModel() # Emite señales cuando cambia la selección de la tabla
        sel_modelo.currentRowChanged.connect(self.fila_seleccionada_cambia) # emite señal cuando cambia la fila seleccionada
        # envía la fila actual seleccionada y la anterior seleccionada (current,previous)

    def fila_seleccionada_cambia(self, current, previous):
        """
        current = nueva fila seleccionada
        previous = fila seleccionada anterior
        Leemos los datos de la fila actual del modelo y los mostramos
        """
        if not current.isValid():
            print("Sin selección")
            return
        
        fila = current.row()

        # Leemos directamente del modelo base (self.modelo)
        # no de la vista (self.tabla), porque la vista puede tener filtros o
        # estar ordenada de fora diferente. Por eso usamos current.row()
        # para obtener la fila correcta en el modelo base
        idx_nombre = self.modelo.index(fila, 1) # columna 'nombre'
        idx_telefono = self.modelo.index(fila, 2) # columna 'telefono'
        idx_email = self.modelo.index(fila, 3) # columna 'email'

        nom = self.modelo.data(idx_nombre)
        tlf = self.modelo.data(idx_telefono)
        mail = self.modelo.data(idx_email)

        print("Fila seleccionada:")
        print("- Nombre  :", nom)
        print("- Teléfono:", tlf)
        print("- Email   :", mail)

        # Mostramos en StatusBar la fila seleccionada
        self.statusBar().showMessage(f"Selección: {nom} ({mail})")


    def aniadir_contacto(self):
        """Abre el diálogo y añade un contacto si se acepta."""
        # Diálogo propio
        dialogo = DialogoContacto(self)

        # exec() bloquea hasta Aceptar/Cancelar 
        if dialogo.exec():
            nombre, telefono, email = dialogo.datos()

            # Guardamos en la base de datos mediante insertar_contacto_bd
            nuevo_id = self.insertar_contacto_bd(nombre, telefono, email) # Función que inserta el contacto en la BD
            if nuevo_id == -1:
                return # Si falla no se añade a la memoria
            self.modelo.select() # Actualizamos la tabla
            
            # Guardamos en memoria para mostrarlo
            contacto = {
                "id": int(nuevo_id),
                "nombre": nombre,
                "telefono": telefono,
                "email": email,
            }
            self.contactos.append(contacto) 
            
            # Refrescamos vista + estado + dock
            self.actualizar_lista()
            self.actualizar_estado()
            self.actualizar_dock("Añadir", contacto)


    # La configuración de la tabla, oculta el ID, hecho que oculta el parámetro necesitado
    # para eliminar un contacto de la BD. En un principio pensé que era buena idea, modificar
    # el método eliminar_contacto(), para que tomara el número de fila de tabla para eliminar
    # el contacto. Posteriormente he pensado dejar ID como parámetro de borrado, haciendo 
    # necesario el acceso a la base de datos para poder borrar un contacto.
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
        
        # Si se confirma, borramos en BD
        if not self.borrar_contacto_bd(encontrado["id"]): # Función que elimina el contacto de la BD
            return # si falla, no tocamos el contacto
        self.modelo.select() # Actualizamos la tabla

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

    def conectar_bd(self):
        """
        Abre o crea la BD SQLite en el archivo local SQLite/contactos.db y deja la 
        conexión abierta en self.db para usarla en todo el programa.
        """

        # Carpeta donde está este .py
        base = Path(__file__).resolve().parent

        # Creamos carpeta SQLite al lado del .py
        carpeta = base / "SQLite"
        carpeta.mkdir(parents=True, exist_ok=True)

        # Ruta completa al archivo .db
        ruta_db = carpeta / "contactos.db"

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(str(ruta_db))

        if not self.db.open():
            QMessageBox.critical(
                self,
                "Error BD",
                "No se ha podido abrir la BD SQLite/contactos.db"
            )
            sys.exit(1)

    def creamos_tabla_si_no_existe(self):
        # Crea la tabla contactos si aún no existe
        consulta = QSqlQuery()
        consulta.exec(
            """
            CREATE TABLE IF NOT EXISTS contactos
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(40) NOT NULL,
                telefono INTEGER(9),
                email VARCHAR(50) NOT NULL
            )
            """
        )
    
    def insertar_contacto_bd(self, nombre:str, telefono:str, email:str) -> int:
        """
        Inserta un contacto en la base de datos y devuelve el id generado (AUTOINCREMENT)
        """
        q = QSqlQuery()
        q.prepare("""
            INSERT INTO contactos (nombre, telefono, email)
            VALUES (?, ?, ?)
        """)
        q.addBindValue(nombre)
        q.addBindValue(telefono)
        q.addBindValue(email)

        if not q.exec():
            QMessageBox.critical(self, "Error", "No se pudo insertar en BD:\n" + q.lastError().text())
            return -1
        
        # Devuelve el ID generado
        return q.lastInsertId()
    
    def cargar_contactos_desde_bd(self):
        self.contactos.clear() # Vacía la lista dde memoria para volver a llenarla con los datos de la bd

        q = QSqlQuery() # Crea una consulta a la db
        if not q.exec("SELECT id, nombre, telefono, email FROM contactos ORDER BY id"):
            QMessageBox.critical(self, "Error", "No se pudo leer la BD:\n" + q.lastError().text())
            return

        while q.next(): # Recorre cada fila devuelta por el SELECT y la añade a self.contactos para mostrarla en el QListWidget
            self.contactos.append({
                "id": int(q.value(0)),
                "nombre": str(q.value(1)),
                "telefono": str(q.value(2) or ""),
                "email": str(q.value(3)),
            })

    def borrar_contacto_bd(self, id_contacto:int) -> bool:
        """
        Borrar en la BD el contacto mediante el id. Devuelve True si se borró
        """
        q = QSqlQuery()
        q.prepare("DELETE FROM contactos WHERE id = ?")
        q.addBindValue(id_contacto)

        if not q.exec():
            QMessageBox.critical(self,  "Error", "No se pudo borrar en BD:\n" + q.lastError().text())
            return False
        
        return True


if __name__ == "__main__":
    # Punto de entrada típico de Qt: QApplication -> ventana -> show -> exec()
    app = QApplication(sys.argv)

    # Creamos y mostramos la ventana principal
    window = MainWindow()
    window.resize(700, 400)  # Tamaño inicial cómodo
    window.show()

    # Arrancamos el bucle principal de eventos
    sys.exit(app.exec())
