import os
import pymysql
from flask import Flask

# Configurações do banco de dados
DB_HOST = os.getenv('DB_HOST', 'mariadb')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'alunos_db')

# Função para conectar ao banco de dados
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
