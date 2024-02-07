# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(617, 592)
        login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 40, 451, 501))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 66);\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setGeometry(QRect(90, 310, 281, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.txt_user.setFont(font)
        self.txt_user.setStyleSheet(u"background-color: rgb(136, 136, 136);\n"
"color: rgb(0, 108, 0);")
        self.txt_user.setAlignment(Qt.AlignCenter)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(90, 370, 281, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.txt_senha.setFont(font1)
        self.txt_senha.setStyleSheet(u"background-color: rgb(136, 136, 136);\n"
"color: rgb(0, 108, 0);")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(170, 430, 121, 41))
        font2 = QFont()
        font2.setPointSize(13)
        self.btn_login.setFont(font2)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color:  green;\n"
"color: rgb(0,0,0);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color:  white;\n"
"color: green;\n"
"border-radius:10px;\n"
"\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 221, 231))
        self.label.setPixmap(QPixmap(u"_img/login.jpg"))
        self.label.setScaledContents(True)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("login", u"USUARIO", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("login", u"SENHA", None))
        self.btn_login.setText(QCoreApplication.translate("login", u"LOGIN", None))
        self.label.setText("")
    # retranslateUi

