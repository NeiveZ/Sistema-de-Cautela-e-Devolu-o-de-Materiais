from os import access
from django.contrib.auth import logout
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from numpy import equal
from xml_files import ReadXml
from PySide6.QtWidgets import(QApplication, QFileDialog,
 QMainWindow, QMessageBox, QTreeWidgetItem, QWidget)
from ui_login import Ui_login
from ui_main import Ui_MainWindow
import sys
from datetime import date
from database import DataBase
from xml_files import ReadXml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt


class Login(QWidget, Ui_login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0 
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema") 
        appIcon = QIcon('_imgs/icone.PNG')
        self.setWindowIcon(appIcon)
        
        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):

        self.users = DataBase()
        self.users.conecta()
        autenticado =  self.users.check_user(self.txt_user.text().upper(), self.txt_senha.text())

        if autenticado.lower() == "cmt_ferramental" or autenticado.lower() == "user":
            
            self.w = MainWindow(self.txt_user.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:    
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou Senha Incorreto \n \n Tentativa: {self.tentativas +1} de 3')
                msg.exec()
                self.tentativas +=1
            if self.tentativas == 3:
                #bloquear usuario
                self.users.close_connection()
                sys.exit(0)    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Cautela")

        self.user = username
        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

        #*************************PAGINAS DO SISTEMA********************************************
        self.btn_home.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_home))
        self.btn_ferramentas.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.pages.setCurrentWidget(self.pg_import)) 

        self.btn_cadastrar.clicked.connect(self.subscrive_user)
        self.btn_logout.clicked.connect(self.logout)

        #ARQUIVO XML
        self.btn_open.clicked.connect(self.open_path)
        self.btn_import.clicked.connect(self.import_xml_files)

        #Filtro
        self.txt_filtro.textChanged.connect(self.update_filter)


     #gerar saida e estorno
        self.btn_saida.clicked.connect(self.gerar_saida)
        self.btn_devolucao.clicked.connect(self.gerar_estorno)

        self.btn_excel.clicked.connect(self.excel_file)
        self.btn_grafico.clicked.connect(self.graphic)
        self.reset_table()

    def subscrive_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(" Senhas Diferentes")
            msg.setText("A senha não é igual!")
            msg.exec()
            return None

        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
        access = self.cb_perfil.currentText()
        su = self.cb_su.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access, su)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Cadastro de Usuario")
        msg.setText("Cadastro realizado com sucesso!")
        msg.exec()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")

    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                          "/home",
                                                          QFileDialog.ShowDirsOnly
                                       
                                                          | QFileDialog.DontResolveSymlinks)
        self.txt_file.setText(self.path)
    def import_xml_files(self):

        xml = ReadXml(self.txt_file.text())
        all = xml.all_files()
        self.progressBar.setMaximum(len(all))  
        db = DataBase()
        db.conecta()
        cont = 1

        for i in all:
            self.progressBar.setValue(cont)
            fullDataSet = xml.nfe_data(i)
            db.insert_data(fullDataSet)
            cont+=1  
        
        #ATUALIZA A TABELA

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importação XML")
        msg.setText("importação concluída!")
        msg.exec()
        self.progressBar.setValue(0)

        db.close_connection()    

    def table_estoque(self):
        self.tw_estoque.setStyleSheet(u" QHeaderView{ color:black}; color:#fff; font-size: 15px")
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query(f"SELECT * FROM Notas WHERE data_saida = '' ", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)    

                self.x = i[0] 
        self.tw_estoque.setSortingEnabled(False)

        for i in range(1, 12):
            self.tw_estoque.resizeColumnToContents(i)       

    def table_saida(self):
        self.tw_saida.setStyleSheet(u" QHeaderView{ color:black}; color:#fff; font-size: 15px")
        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query(f"""SELECT Mat, Loc, Det, CProd,XProd, uCom, Usuario, data_saida  
                                    from Notas WHERE data_saida != '' """, cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            #faz o check para identificar a mesma nota e adicionar um nivel
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_saida, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)    

                self.x = i[0] 
        self.tw_saida.setSortingEnabled(False)

        for i in range(1, 12):
            self.tw_saida.resizeColumnToContents(i)  

    def table_geral(self):

        self.tb_geral.setStyleSheet(u" QHeaderView{ color:black}; color:#fff;font-size: 15px;") 
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("system.db")
        db.open()
        
        self.model = QSqlTableModel(db=db)
        self.tb_geral.setModel(self.model)
        self.model.setTable("Notas")
        self.model.select()

    def reset_table(self):
        self.tw_estoque.clear()
        self.tw_saida.clear()

        self.table_saida()
        self.table_estoque()
        self.table_geral()

    def update_filter(self, s):
        s = re.sub("[\\W_]+", "", s)
        filter_str = 'CProd LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)
        self.model.select() 
    
    def gerar_saida(self):

        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items_out.append(child.text(0))
    
        recurse(self.tw_estoque.invisibleRootItem())

        #Pergunta se usuario realmente deseja fazer is.
        self.question('saída')

    def gerar_estorno(self):
        
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == QtCore.Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.tw_saida.invisibleRootItem())
        self.question('estorno')      

    def question(self, table):

        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText("As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estorno(self.checked_items)
                self.db.close_connection()
                self.reset_table()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conecta()
                self.db.update_estoque(data_saida, self.user, self.checked_items_out)
                self.db.close_connection()
                self.reset_table()

    def excel_file(self):

        cnx = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo de Cautela.xlsx", sheet_name='Notas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Cautela")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec()

    def graphic(self):

        cnx = sqlite3.connect("system.db")
        estoque = pd.read_sql_query('SELECT * FROM Notas', cnx)
        saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        fig1, axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()




    def logout(self):
        # Adicione a lógica de logout aqui
        self.current_user = None
        # Por exemplo, você pode fechar a janela atual e exibir a janela de login novamente
        # Feche a janela atual
        self.close()
        
        self.login_window = Login()
        self.login_window.show()

       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()
