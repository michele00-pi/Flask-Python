import sqlite3 as sql

def conectar():
    conn =  sql.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela(conn, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS Musicas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, tempo TEXT, tipo TEXT)")
    conn.commit()

def inserir_dados(conn,cursor,nome,tempo,tipo):
    cursor.execute("INSERT INTO Musicas(nome,tempo,tipo) VALUES(?,?,?)", (nome,tempo,tipo))
    conn.commit()

def buscar_dados(cursor, tipo):
    cursor.execute("SELECT nome, tempo FROM Musicas WHERE tipo = ?", (tipo,))
    dados = cursor.fetchall()
    return dados

def limpar_tabela(conn, cursor):
    cursor.execute("DELETE FROM Musicas")
    conn.commit()