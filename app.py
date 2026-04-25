from flask import Flask, render_template, request
import sqlite3
import database.dbFunctions as db

conn, cursor = db.conectar()
db.criar_tabela(conn=conn, cursor=cursor)

app = Flask(__name__)

dict_gringo = {"Nome": [], "Tempo": []}
dict_classico = {"Nome": [], "Tempo": []}

@app.route("/") #Pagina inicial

def main():
    conn, cursor = db.conectar()
    db.criar_tabela(conn=conn, cursor=cursor)
    return render_template("main.html")

@app.route("/brasileira", methods=["POST", "GET"]) #Rota das musicas brasileiras

def page_brasileira():
    conn, cursor = db.conectar() #Tem que deixar dentro da rota, se deixar global quebra
    tipo = "Brasileira"
    dados = db.buscar_dados(cursor=cursor, tipo=tipo)
    if request.method == 'POST':

        Btn = request.form.get("Btn")

        if Btn == "limpar":
            db.limpar_tabela(conn=conn, cursor=cursor)
            dados=[()]

        elif Btn == "listar":
            nome = request.form.get("BRASILINPUT")
            tempo = request.form.get("TEMPOINPUT")
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo) #Insere  na tabela "Musicas" 
            dados = db.buscar_dados(cursor=cursor,tipo=tipo)
        
        conn.close()
    return render_template("brasileira.html", dados=dados)


@app.route("/estrangeira", methods=["POST", "GET"]) #Rota das musicas estrangeiras

def page_estrangeira():
    conn, cursor = db.conectar()
    tipo = "Estrangeira"
    dados = db.buscar_dados(cursor=cursor, tipo=tipo)
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(dict_gringo)
            db.limpar_tabela(conn=conn, cursor=cursor)
            dados=[()]

        elif Btn == "listar":
            nome = request.form.get("ESTRANGEIROINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, dict=dict_gringo)
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
            dados = db.buscar_dados(cursor=cursor, tipo=tipo)
        
        conn.close()
    return render_template("estrangeira.html", dict_gringo=dict_gringo)

@app.route("/classica", methods=["POST", "GET"]) #Rota das musicas classicas

def page_classica():
    conn, cursor = db.conectar()
    tipo = "Classica"
    dados = db.buscar_dados(cursor=cursor, tipo=tipo)
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(dict_classico)
            db.limpar_tabela(conn=conn, cursor=cursor)
            dados = [()]
    
        elif Btn == "listar":
            nome = request.form.get("CLASSICOINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, dict=dict_classico)
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
            dados = db.buscar_dados(cursor=cursor, tipo=tipo)
            
        conn.close()
    return render_template("classica.html", dict_classico=dict_classico)

def cadastrar(nome,tempo, dict):

    dict["Nome"].append(nome)
    dict["Tempo"].append(tempo)

def limpar(dict):

    dict["Nome"].clear()
    dict["Tempo"].clear()

if __name__ == "__main__":
    app.run(debug=True)