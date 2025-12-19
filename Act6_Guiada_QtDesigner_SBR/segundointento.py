# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segundointento.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"/* ===== Ventana y widgets generales ===== */\n"
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
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Soy una subventana", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Cerrar", None))
    # retranslateUi

