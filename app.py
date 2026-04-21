from flask import Flask, render_template, request
import sqlite3
import database.dbFunctions

app = Flask(__name__)

lista_brasil = []
lista_gringo = []
lista_classico = []

@app.route("/") #Pagina inicial

def main():
    return render_template("main.html")

@app.route("/brasileira", methods=["POST", "GET"]) #Pagina das musicas brasileiras

def page_brasileira():
        
    if request.method == 'POST':

        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(lista_brasil)

        elif Btn == "listar":
            nome = request.form.get("BRASILINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista_brasil)
        
    return render_template("brasileira.html", lista_brasil=lista_brasil)


@app.route("/estrangeira", methods=["POST", "GET"]) #Pagina das musicas estrangeiras

def page_estrangeira():

    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            limpar(lista_gringo)

        elif Btn == "listar":
            nome = request.form.get("ESTRANGEIROINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista_gringo)
        
    return render_template("estrangeira.html", lista_gringo=lista_gringo)

@app.route("/classica", methods=["POST", "GET"]) #Pagina das musicas classicas

def page_classica():
    
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
             limpar(lista_classico)
    
        elif Btn == "listar":
            nome = request.form.get("CLASSICOINPUT")
            tempo = request.form.get("TEMPOINPUT")
            cadastrar(nome, tempo, lista=lista_classico)
           
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