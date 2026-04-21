import sqlite3 as sql

def conectar():
    conn =  sql.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela(database, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Musicas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, tempo TEXT, tipo TEXT)")