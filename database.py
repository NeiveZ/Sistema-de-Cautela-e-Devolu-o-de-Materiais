import sqlite3
from sqlite3.dbapi2 import Cursor


class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name
    def conecta(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass


    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(
                           
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        user TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        access TEXT NOT NULL,
                        su   TEXT NOT NULL

                ); 

            """)
        except AttributeError:
            print("Faça conexão")

    def insert_user(self, name, user, password, access, su):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""

            INSERT INTO users(name, user, password, access, su) VALUES(?,?,?,?,?)
        
        """,(name,user, password, access, su))
            self.connection.commit()
        except AttributeError:
            print("Erro de conexão")      

    def check_user(self, user, password):

        try:

            cursor = self.connection.cursor()
            cursor.execute("""
            
            SELECT * FROM users;

            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "cmt_ferramental":
                    return "cmt_ferramental"
               
                elif linha[2].upper() == user.upper() and linha[3] == password and linha[4] == "usuario":
                    return "user"

                else:
                    continue  
            return "sem acesso"

        except:
            pass      

    def insert_data(self, full_dataset):

        cursor = self.connection.cursor()
    
        campos_tabela = (
        'Mat','Loc', 'Ico', 'Nr', 'Det', 'CProd', 'QCom', 'XProd', 'UCom','DataEmissao', 'data_saida', 'Usuario')
    
        qntd = ','.join(map(str, '?' * 12))
        query = f"""INSERT INTO Notas {campos_tabela} VALUES({qntd})""" # Correção aqui

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()
        except sqlite3.IntegrityError:
            print('Nota já existe no banco')
      

    def create_table_nfe(self):

        cursor = self.connection.cursor()

        cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS Notas(

            Mat TEXT,        
            Loc TEXT,
            Ico TEXT,
            Nr TEXT,
            Det TEXT,
            CProd TEXT,
            QCom TEXT,                
            XProd TEXT,
            UCom TEXT,          
            DataEmissao TEXT,
            data_saida TEXT,
            Usuario TEXT,           
            
            PRIMARY KEY ( Mat)
          );

        """)
    def update_estoque(self, data_saida, user, notas):
        try:
            with self.connection:
                cursor = self.connection.cursor()
                for nota in notas:
                    cursor.execute(f"UPDATE Notas SET data_saida = ?, usuario = ? WHERE Mat = ?", (data_saida, user, nota))
                    self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar a consulta SQL para atualizar estoque: {e}")

    
    def update_estorno(self, notas):
        try:
            with self.connection:
                cursor = self.connection.cursor()
            for nota in notas:
                sql_query = "UPDATE Notas SET data_saida = '' WHERE Mat = ?"
                print(f"Consulta SQL: {sql_query}, Mat: {nota}")
                cursor.execute(sql_query, (nota,))
            # Mova o commit para fora do loop
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar a consulta SQL para estorno: {e}")

if __name__ == "__main__":

    db = DataBase()
    db.conecta()
    db.create_table_users()
    db.create_table_nfe()
    db.close_connection()
