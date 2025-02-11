from math import e
import mysql.connector as mc# Biblioteca do conector do MySQL
from mysql.connector import Error # Importanto a classe Error para tratar as mensagens de erro do código
from dotenv import load_dotenv # Importando a função load_dotenv 
from os import getenv # Importando a função getenv

class Database:
    def __init__(self):
        load_dotenv()
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PSWD')
        self.database = getenv('DB_NAME')
        self.connection = None # Inicialização da conexão
        self.cursor = None # Inicialização do cursor

    def conectar(self):
        """Estabelece uma conexão com o banco de dados."""
        try: 
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password  

            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print("conexao como banco de ados realizada com sucesso!")
        except Error as e:
            print(f"erro de conexao: {e}")
            self.connection = None
            self.cursor = None

    def desconectar(self):
        """encerra a conexao com o banco de dados e o cursor, se existirem."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados encerrada com sucesso!")

    def executar(self, sql, params):
        """execua uma instrucao no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexao ao banco de dados nao estabelecida.')
            return None
        
        try:
            self.cursor.execute(sql, params)
            self.cursor.commit()
            return self.cursor
        except Error as e:
            print(f"Erro ao executar a instrucao: {e}")
            return None
        
    def consultar(self, sql, params):
        """execua uma instrucao no banco de dados."""
        if self.connection is None and self.cursor is None:
            print('Conexao ao banco de dados nao estabelecida.')
            return None
        
        try:
            self.cursor.execute(sql, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Erro ao executar a instrucao: {e}")
            return None