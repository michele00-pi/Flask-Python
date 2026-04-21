from flask import Flask, render_template, request
import sqlite3
import database.dbFunctions as db

conn, cursor = db.conectar()
db.criar_tabela(conn=conn, cursor=cursor)

app = Flask(__name__)

lista_brasil = []
lista_gringo = []
lista_classico = []

@app.route("/") #Pagina inicial

def main():
    return render_template("main.html")

@app.route("/brasileira", methods=["POST", "GET"]) #Rota das musicas brasileiras

def page_brasileira():
    tipo = "Brasileira"
    if request.method == 'POST':

        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(lista_brasil)
            db.limpar_tabela(conn=conn, cursor=cursor)

        elif Btn == "listar":
            nome = request.form.get("BRASILINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista_brasil)
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo) #Insere  na tabela "Musicas" 
            dados = db.buscar_dados(cursor=cursor, tipo=tipo)
        
    return render_template("brasileira.html", lista_brasil=lista_brasil)


@app.route("/estrangeira", methods=["POST", "GET"]) #Rota das musicas estrangeiras

def page_estrangeira():
    tipo = "Estrangeira"
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(lista_gringo)
            db.limpar_tabela(conn=conn, cursor=cursor)

        elif Btn == "listar":
            nome = request.form.get("ESTRANGEIROINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista_gringo)
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
        
    return render_template("estrangeira.html", lista_gringo=lista_gringo)

@app.route("/classica", methods=["POST", "GET"]) #Rota das musicas classicas

def page_classica():
    tipo = "Classica"
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(lista_classico)
            db.limpar_tabela(conn=conn, cursor=cursor)
    
        elif Btn == "listar":
            nome = request.form.get("CLASSICOINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista=lista_classico)
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
           
    return render_template("classica.html", lista_classico=lista_classico)

def cadastrar(nome,tempo, lista):

    lista.append(
        {
            "Nome":nome,
            "Tempo": tempo
        }
    )

def limpar(lista):

    lista.clear()

if __name__ == "__main__":
    app.run(debug=True)