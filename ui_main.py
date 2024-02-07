# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableView,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1461, 921)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font = QFont()
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	border-color: rgb(0, 170, 0);\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.gridLayout_2.addWidget(self.btn_home, 0, 0, 1, 1)

        self.btn_pg_import = QPushButton(self.frame)
        self.btn_pg_import.setObjectName(u"btn_pg_import")
        self.btn_pg_import.setMinimumSize(QSize(0, 30))
        self.btn_pg_import.setSizeIncrement(QSize(0, 0))
        self.btn_pg_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_import.setStyleSheet(u"QPushButton{\n"
"	border-color: rgb(0, 170, 0);\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.gridLayout_2.addWidget(self.btn_pg_import, 0, 1, 1, 1)

        self.btn_ferramentas = QPushButton(self.frame)
        self.btn_ferramentas.setObjectName(u"btn_ferramentas")
        self.btn_ferramentas.setMinimumSize(QSize(0, 30))
        self.btn_ferramentas.setSizeIncrement(QSize(0, 30))
        self.btn_ferramentas.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ferramentas.setStyleSheet(u"QPushButton{\n"
"	border-color: rgb(0, 170, 0);\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.gridLayout_2.addWidget(self.btn_ferramentas, 0, 2, 1, 1)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setBaseSize(QSize(0, 30))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.gridLayout_2.addWidget(self.btn_sobre, 0, 3, 1, 1)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 30))
        self.btn_contato.setBaseSize(QSize(0, 30))
        self.btn_contato.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.gridLayout_2.addWidget(self.btn_contato, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(0, 0, 185);\n"
"border-color: rgb(0, 0, 0);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_10 = QVBoxLayout(self.pg_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 185);")

        self.verticalLayout_10.addWidget(self.label)

        self.btn_logout = QPushButton(self.pg_home)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 30))
        self.btn_logout.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_logout.setFont(font1)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setStyleSheet(u"QPushButton{\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color:  rgb(255,255,255);\n"
"color:black;\n"
"\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_logout)

        self.btn_pg_cadastro = QPushButton(self.pg_home)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")
        self.btn_pg_cadastro.setMinimumSize(QSize(0, 27))
        self.btn_pg_cadastro.setFont(font1)
        self.btn_pg_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pg_cadastro.setStyleSheet(u"QPushButton{\n"
"	color: #fff;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color:  rgb(255,255,255);\n"
"color:black;\n"
"\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_pg_cadastro)

        self.pages.addWidget(self.pg_home)
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_8 = QVBoxLayout(self.pg_table)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.TabWidget = QTabWidget(self.pg_table)
        self.TabWidget.setObjectName(u"TabWidget")
        self.TabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        font2 = QFont()
        font2.setPointSize(12)
        self.tables.setFont(font2)
        self.verticalLayout_9 = QVBoxLayout(self.tables)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")

        self.verticalLayout_5.addWidget(self.label_2)

        self.tw_estoque = QTreeWidget(self.tables)
        font3 = QFont()
        font3.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(8, font3);
        __qtreewidgetitem.setFont(7, font3);
        __qtreewidgetitem.setFont(6, font3);
        __qtreewidgetitem.setFont(5, font3);
        __qtreewidgetitem.setFont(4, font3);
        __qtreewidgetitem.setFont(3, font3);
        __qtreewidgetitem.setFont(2, font3);
        __qtreewidgetitem.setFont(1, font3);
        __qtreewidgetitem.setFont(0, font3);
        self.tw_estoque.setHeaderItem(__qtreewidgetitem)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setMinimumSize(QSize(0, 0))
        self.tw_estoque.setLayoutDirection(Qt.LeftToRight)
        self.tw_estoque.setStyleSheet(u"")
        self.tw_estoque.setTextElideMode(Qt.ElideMiddle)

        self.verticalLayout_5.addWidget(self.tw_estoque)

        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tables)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setFont(7, font3);
        __qtreewidgetitem1.setFont(6, font3);
        __qtreewidgetitem1.setFont(5, font3);
        __qtreewidgetitem1.setFont(4, font3);
        __qtreewidgetitem1.setFont(3, font3);
        __qtreewidgetitem1.setFont(2, font3);
        __qtreewidgetitem1.setFont(1, font3);
        __qtreewidgetitem1.setFont(0, font3);
        self.tw_saida.setHeaderItem(__qtreewidgetitem1)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_5.addWidget(self.tw_saida)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_saida = QPushButton(self.frame_2)
        self.btn_saida.setObjectName(u"btn_saida")
        self.btn_saida.setMinimumSize(QSize(100, 27))
        self.btn_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saida.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-radius: 10px;\n"
"	font-size:16px;	\n"
"	background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_saida)

        self.btn_devolucao = QPushButton(self.frame_2)
        self.btn_devolucao.setObjectName(u"btn_devolucao")
        self.btn_devolucao.setMinimumSize(QSize(100, 27))
        self.btn_devolucao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_devolucao.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"border-radius: 10px;\n"
"font-size:16px;\n"
"background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_devolucao)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_att = QPushButton(self.frame_2)
        self.btn_att.setObjectName(u"btn_att")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_att.sizePolicy().hasHeightForWidth())
        self.btn_att.setSizePolicy(sizePolicy)
        self.btn_att.setMinimumSize(QSize(100, 27))
        self.btn_att.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_att.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"border-radius: 10px;\n"
"font-size:16px;\n"
"background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_att)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(self.tables)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_9.addWidget(self.widget)

        self.TabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setPointSize(20)
        self.label_19.setFont(font4)

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_grafico = QPushButton(self.tab_2)
        self.btn_grafico.setObjectName(u"btn_grafico")
        self.btn_grafico.setMinimumSize(QSize(0, 30))
        self.btn_grafico.setFont(font)
        self.btn_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grafico.setStyleSheet(u"QPushButton{\n"
"	border-color: rgb(0, 170, 0);\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.horizontalLayout_12.addWidget(self.btn_grafico)

        self.btn_excel = QPushButton(self.tab_2)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(0, 30))
        self.btn_excel.setSizeIncrement(QSize(0, 0))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton{\n"
"	border-color: rgb(0, 170, 0);\n"
"	color: rgb(255,255,255);\n"
"border-radius: 1px;\n"
"font-size:16px;\n"
"background-color:rgb(0, 80, 121);\n"
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

        self.horizontalLayout_12.addWidget(self.btn_excel)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.txt_filtro = QLineEdit(self.tab_2)
        self.txt_filtro.setObjectName(u"txt_filtro")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.txt_filtro.setFont(font5)
        self.txt_filtro.setStyleSheet(u"color:white;")
        self.txt_filtro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.txt_filtro)

        self.tb_geral = QTableView(self.tab_2)
        self.tb_geral.setObjectName(u"tb_geral")

        self.verticalLayout_12.addWidget(self.tb_geral)

        self.TabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.TabWidget)

        self.pages.addWidget(self.pg_table)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_2 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_15 = QLabel(self.pg_cadastro)
        self.label_15.setObjectName(u"label_15")
        font6 = QFont()
        font6.setPointSize(25)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.label_15.setFont(font6)
        self.label_15.setStyleSheet(u"background-color: rgb(0, 0, 185);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_15)

        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setPointSize(18)
        font7.setItalic(True)
        self.label_7.setFont(font7)
        self.label_7.setStyleSheet(u"background-color: rgb(0, 0, 185);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(50, -1, -1, -1)
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_nome = QLineEdit(self.pg_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_8.addWidget(self.txt_nome)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, -1, -1, -1)
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.txt_usuario = QLineEdit(self.pg_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")

        self.horizontalLayout_7.addWidget(self.txt_usuario)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(50, -1, -1, -1)
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.txt_senha = QLineEdit(self.pg_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(50, -1, -1, -1)
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.txt_senha_2 = QLineEdit(self.pg_cadastro)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setStyleSheet(u"color: rgba(211,239,251,1);\n"
"border-bottom: 1px solid white;\n"
"border-radius: None;\n"
"background-color: rgba(85, 115, 155,0.1);\n"
"font-size:21px;")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.txt_senha_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, -1, -1, -1)
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.cb_su = QComboBox(self.pg_cadastro)
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.addItem("")
        self.cb_su.setObjectName(u"cb_su")
        self.cb_su.setFont(font1)
        self.cb_su.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_su)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setFont(font1)
        self.cb_perfil.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cb_perfil)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_10.addWidget(self.label_14)

        self.btn_cadastrar = QPushButton(self.pg_cadastro)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"border-radius: 10px;\n"
"font-size:16px;\n"
"background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.horizontalLayout_10.addWidget(self.btn_cadastrar)

        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.pages.addWidget(self.pg_cadastro)
        self.pg_import = QWidget()
        self.pg_import.setObjectName(u"pg_import")
        self.verticalLayout_11 = QVBoxLayout(self.pg_import)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.pg_import)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_11.addWidget(self.label_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.txt_file = QLineEdit(self.pg_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 28))
        self.txt_file.setFont(font2)
        self.txt_file.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_import)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 30))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"	border-top-right-radius:15px;	\n"
"	font-size:16px;\n"
"	background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_open)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.pg_import)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.btn_import = QPushButton(self.pg_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(0, 28))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,10);\n"
"border-radius: 10px;\n"
"font-size:16px;\n"
"background-color: #fff;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(170,255,255);\n"
"color: black;\n"
"\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_import)

        self.label_18 = QLabel(self.pg_import)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.progressBar = QProgressBar(self.pg_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setStyleSheet(u"QProgressBar{	background-color: rgba(0, 0, 0,0.1);\n"
"                    	color: rgb(255, 255, 255);\n"
"                		border-style: none;\n"
"                		text-align: center;\n"
"                		border-radius:10px;\n"
"                \n"
"                }\n"
" \n"
"               \n"
"QProgressBar::chunk{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 75, 149, 255), stop:1 rgba(72, 130, 157, 255));\n"
"                				border-radius:10px;\n"
"                                }")
        self.progressBar.setInputMethodHints(Qt.ImhNone)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_11.addWidget(self.progressBar)

        self.pages.addWidget(self.pg_import)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_16 = QLabel(self.pg_contato)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setStyleSheet(u"background-color: rgb(0, 0, 185);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_16)

        self.label_20 = QLabel(self.pg_contato)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font6)
        self.label_20.setStyleSheet(u"background-color: rgb(0, 0, 185);")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_20)

        self.pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_17 = QLabel(self.pg_sobre)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 50))
        self.label_17.setFont(font4)

        self.verticalLayout_13.addWidget(self.label_17)

        self.label_4 = QLabel(self.pg_sobre)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_4)

        self.pages.addWidget(self.pg_sobre)

        self.gridLayout.addWidget(self.pages, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(1)
        self.TabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_pg_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.btn_ferramentas.setText(QCoreApplication.translate("MainWindow", u"FERRAMENTAS", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"CONTATO", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#aaaa00;\">FERRAMENTAL</span></p><p align=\"center\"><span style=\" font-weight:600; color:#aaaa00;\"><br/></span><span style=\" font-size:20pt; font-weight:600; color:#aaaa00;\">ESQUADRILHA DE MANUTEN\u00c7\u00c3O E SUPRIMENTO</span></p><p align=\"center\"><img src=\"_img/logo.png\"/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">ESTOQUE</span></p></body></html>", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"Medida", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descricao ou SN", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"MPN", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Ferramenta", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Nr", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Ico", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Loc", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Num.Ferramenta", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SAIDA</p></body></html>", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("MainWindow", u"Data Saida", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"Medida", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Desc. ou SN", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"MPN", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Loc", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Num. Ferramenta", None));
        self.btn_saida.setText(QCoreApplication.translate("MainWindow", u"CAUTELAR", None))
        self.btn_devolucao.setText(QCoreApplication.translate("MainWindow", u"DEVOLVER", None))
        self.btn_att.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">ESTOQUE</span></p></body></html>", None))
        self.btn_grafico.setText(QCoreApplication.translate("MainWindow", u"Gerar Grafico", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.txt_filtro.setText(QCoreApplication.translate("MainWindow", u"FILTRO", None))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"DADOS", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">TELA DE CADASTRO</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\"_img/user.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; font-style:normal; color:#ffffff;\">CADASTRAR USUARIO</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">NOME:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">USUARIO:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SENHA:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">SENHA:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">PERFIL:</span></p></body></html>", None))
        self.cb_su.setItemText(0, QCoreApplication.translate("MainWindow", u"ECAP", None))
        self.cb_su.setItemText(1, QCoreApplication.translate("MainWindow", u"EMS", None))
        self.cb_su.setItemText(2, QCoreApplication.translate("MainWindow", u"1 EHEG", None))
        self.cb_su.setItemText(3, QCoreApplication.translate("MainWindow", u"2 EHEG", None))
        self.cb_su.setItemText(4, QCoreApplication.translate("MainWindow", u"3 EHEG", None))
        self.cb_su.setItemText(5, QCoreApplication.translate("MainWindow", u"BASE", None))
        self.cb_su.setItemText(6, QCoreApplication.translate("MainWindow", u"Est.Maior", None))
        self.cb_su.setItemText(7, QCoreApplication.translate("MainWindow", u"FAB", None))
        self.cb_su.setItemText(8, QCoreApplication.translate("MainWindow", u"MARINHA", None))

        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"usuario", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"cmt_ferramental", None))

        self.label_14.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_13.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta com os arquivos XML -------->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"ABRIR", None))
        self.label_6.setText("")
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"IMPORTAR", None))
        self.label_18.setText("")
#if QT_CONFIG(statustip)
        self.progressBar.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\"> CONTATO</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Desenvolvedor: Lucas Neves Teixeira</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ffffff;\">SOBRE</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">ESTE SISTEMA FOI CRIADO PARA AUXILIAR NO CONTROLE DE ENTRADA E SAIDA DE FERRAMENTAS</span></p></body></html>", None))
    # retranslateUi

