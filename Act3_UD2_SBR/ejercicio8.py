# Ejercio 8 
# Menú lateral con QStackedWidget:
#   - Página "Inici": camnbia el texto al pulsar el botón.
#   - Página "Informació": abre la web del IES paco Mollá.
#   - Página "Configuració": muestra por consola el estado de varios checkbox

import sys
# Importamos todos los widgets y layouts que vamos a utilizar en la interfaz
from PySide6.QtWidgets import (QApplication, QWidget, QListWidget, QStackedWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox)
# QDesktopServices y QUrl se usan para abrir una página web externa en el navegador
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        # Titulo de lventana
        self.setWindowTitle("Menú lateral amb QStackedWidget")

        # Tamaño aproximado de la ventana
        self.resize(800, 300)

        # Creamos y organizamos la interfaz
        self.crear_interfaz()
    
    def crear_interfaz(self):
        # Layout principal horizontal
        # [lista lateral] [ contenido (QStackedWidget) ]
        layout_principal = QHBoxLayout(self)

        # --- Menú lateral ---
        # Lista que actuará como menú: cada elemento corresponde a una página del QStackedWidget
        self.menu_lateral = QListWidget()
        self.menu_lateral.addItems(["Inici","Informació", "Configuració"])
        self.menu_lateral.setFixedWidth(150)

        # Cuando cambiamos la fila selecciona, cambamos la página
        # currentRowChanged emite el índice de la fila seleccionada (0, 1, 2, ...)
        self.menu_lateral.currentRowChanged.connect(self.cambiar_pagina)

        # --- QStackedWidget con las 3 páginas ---
        # Contenedor que apila varias páginas y solo muestra una a la vez
        self.stacked = QStackedWidget()

        # Creamos las páginas
        pagina_ini = self.crear_pagina_ini()
        pagina_inf = self.crear_pagina_inf()
        pagina_conf = self.crear_pagina_conf()

        # ñadimos las páginas al QStackedWidget
        # El orden en que se añaden define el índice (0: Inici, 1: Informació, 2: Configuració)
        self.stacked.addWidget(pagina_ini)
        self.stacked.addWidget(pagina_inf)
        self.stacked.addWidget(pagina_conf)

        # Seleccionamos la primera opción del menú
        # Esto hace que al iniciar se muestre la página "Inici"
        self.menu_lateral.setCurrentRow(0)

        # Añadimos Widgets al layout_principal
        layout_principal.addWidget(self.menu_lateral)
        layout_principal.addWidget(self.stacked)

        # Asignamos el layout_principal a la ventana
        self.setLayout(layout_principal)

    # --------------------------------------------------
    #                   PAGINA INICI
    # --------------------------------------------------
    def crear_pagina_ini(self):
        # Creamos el widget que actuará como página y su layout vertical
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        # Etiqueta de bienvenida
        self.lbl_bienvenida = QLabel("Benvingut/da a l'aplicació")

        # QLineEdit + botón el la fila
        self.campo_de_texto = QLineEdit()
        btn_cambiar = QPushButton("Canvia el missatge")

        # Cuando se pulse el botón, cambiaremos el texto de la etiqueta
        # Conectamos la señal clicked del botón con el método cambiar_mensage
        btn_cambiar.clicked.connect(self.cambiar_mensage)

        # Layout horizontal para colocar el QLineEdit y el botón en la misma fila
        layout_fila = QHBoxLayout()
        layout_fila.addWidget(self.campo_de_texto)
        layout_fila.addWidget(btn_cambiar)

        # Añadimos la etiqueta y el layout de la fila al layout principal de la página
        layout.addWidget(self.lbl_bienvenida)
        layout.addLayout(layout_fila)

        # Devolvemos el widget completo que se añadirá al QStackedWidget
        return pagina
    
    
    def cambiar_mensage(self):
        # Cambia el texto de la etiqueta al pulsar el boton.
        # No usamos el contenido del QLineEdit; se pone un texto fijo.
        self.lbl_bienvenida.setText("Has fet clic en el botó")

    # --------------------------------------------------
    #                PAGINA INFORMACIO
    # --------------------------------------------------
    def crear_pagina_inf(self):
        # Creamos el widget que actuará como página y su layout vertical
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        # Etiqueta con el texto informativo
        lbl_info = QLabel("Aquesta app mostra com utilitzar QStackedWidget amb menú lateral.")

        # Botón que abrirá la página web del centro
        btn_web = QPushButton("Obrir wed de IES Paco Mollà")
        # Conectamos el clic del botón con el método que abre la URL en el navegador
        btn_web.clicked.connect(self.abrir_web_paco_molla)

        # Añadimos los widgets al layout
        layout.addWidget(lbl_info)
        layout.addWidget(btn_web)
        # Añadimos un "stretch" para empujar los elementos hacia arriba
        layout.addStretch()

        return pagina
    
    def abrir_web_paco_molla(self):
        # Abre el navegador del Paco Mollà
        # Creamos un objeto QUrl con la dirección del centro
        url = QUrl("https://www.iespacomolla.es") 
        # QDesktopServices se encarga de abrir la URL con el navegador por defecto del sistema
        QDesktopServices.openUrl(url)


    # --------------------------------------------------
    #               PAGINA CONFIGURACIO
    # --------------------------------------------------
    def crear_pagina_conf(self):
        # Creamos el widget que actuará como página y su layout vertical
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        # Checkboxes de configuración
        self.chk_modo_oscuro = QCheckBox("Activar mode fosc")
        self.chk_notificaciones = QCheckBox("Notificacions actives")
        self.chk_auto_update = QCheckBox("Actualitzar automàticament")

        # Botón que mostrará el estado actual de los checkbox por consola
        btn_mostrar = QPushButton("Mostrar selecció")
        # Conectamos el clic del botón con el método que imprime la configuración
        btn_mostrar.clicked.connect(self.mostrar_configuracio)

        # Añadimos los checkbox y el botón al layout
        layout.addWidget(self.chk_modo_oscuro)
        layout.addWidget(self.chk_notificaciones)
        layout.addWidget(self.chk_auto_update)
        layout.addStretch()
        layout.addWidget(btn_mostrar)

        return pagina
    
    def mostrar_configuracio(self):
        # Imprime por consola el estado actual del Checkbox
        # isChecked() devuelve True/False según si el checkbox está marcado
        print("Configuració actual")
        print(f"- Mode fosc: {self.chk_modo_oscuro.isChecked()}")
        print(f"- Notificacions: {self.chk_notificaciones.isChecked()}")
        print(f"- Auto-update: {self.chk_auto_update.isChecked()}")

    # --------------------------------------------------
    # Cambio de página según el menú lateral
    # --------------------------------------------------
    def cambiar_pagina(self, indice):
        # Cambia la página visible del QStackedWidget
        # El índice recibido coincide con la posición de la página en self.stacked
        self.stacked.setCurrentIndex(indice)


if __name__ == "__main__":
    # Creamos la aplicación principal de Qt
    app = QApplication(sys.argv)

    # Creamos la ventana y la mostramos en pantalla
    ventana = VentanaPrincipal()
    ventana.show()

    # Iniciamos el bucle de eventos de la aplicación
    sys.exit(app.exec())





