# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primerintento.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import recursos_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 318)
        icon = QIcon()
        icon.addFile(u":/iconos/icono1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* ===== Ventana y widgets generales ===== */\n"
"QMainWindow, QWidget {\n"
"    background-color: #2b2b2b;\n"
"    color: #f2f2f2;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"/* ===== Label ===== */\n"
"QLabel {\n"
"    color: #f2f2f2;\n"
"    margin-top: 6px;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"/* ===== LineEdit ===== */\n"
"QLineEdit {\n"
"    background-color: #1f1f1f;\n"
"    color: #f2f2f2;\n"
"    border: 1px solid #4a4a4a;\n"
"    border-radius: 3px;\n"
"    padding: 4px 6px;\n"
"    selection-background-color: #f4b400;\n"
"    selection-color: #111111;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #f4b400;\n"
"}\n"
"\n"
"/* ===== Bot\u00f3n Enviar ===== */\n"
"QPushButton {\n"
"    background-color: #f4b400;\n"
"    color: #111111;\n"
"    border: 1px solid #d69c00;\n"
"    border-radius: 3px;\n"
"    padding: 6px 10px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #ffcc33;\n"
"    border: 1px solid #e0a800;\n"
"}\n"
"\n"
"QPushButton:pressed {"
                        "\n"
"    background-color: #d69c00;\n"
"    border: 1px solid #b88400;\n"
"}\n"
"\n"
"/* ===== Men\u00fa superior ===== */\n"
"QMenuBar {\n"
"    background-color: #1e1e1e;\n"
"    color: #f2f2f2;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 4px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* ===== Men\u00fa desplegable ===== */\n"
"QMenu {\n"
"    background-color: #1e1e1e;\n"
"    color: #f2f2f2;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 18px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #f4b400;\n"
"    color: #111111;\n"
"}\n"
"\n"
"/* ===== Barra de estado ===== */\n"
"QStatusBar {\n"
"    background-color: #1e1e1e;\n"
"    color: #f2f2f2;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;\n"
"}\n"
"")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icono2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionSalir.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Primer dise\u00f1o", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(QCoreApplication.translate("MainWindow", u"Etiqueta solicitante con texto", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Introduce", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

