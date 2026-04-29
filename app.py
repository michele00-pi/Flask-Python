from flask import Flask, render_template, request
import sqlite3
import database.dbFunctions as db

app = Flask(__name__)

@app.route("/") #Pagina inicial

def main():
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
            conn.commit()
            dados=[()]

        elif Btn == "listar":
            nome = request.form.get("BRASILINPUT")
            tempo = request.form.get("TEMPOINPUT")
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo) #Insere  na tabela "Musicas" 
            conn.commit()
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
            db.limpar_tabela(conn=conn, cursor=cursor)
            conn.commit()
            dados=[()]

        elif Btn == "listar":
            nome = request.form.get("ESTRANGEIROINPUT")
            tempo = request.form.get("TEMPOINPUT")
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
            conn.commit()
            dados = db.buscar_dados(cursor=cursor, tipo=tipo)
        
        conn.close()
    return render_template("estrangeira.html", dados=dados)

@app.route("/classica", methods=["POST", "GET"]) #Rota das musicas classicas

def page_classica():
    conn, cursor = db.conectar()
    tipo = "Classica"
    dados = db.buscar_dados(cursor=cursor, tipo=tipo)
    if request.method == 'POST':
        Btn = request.form.get("Btn")

        if Btn == "limpar":
            db.limpar_tabela(conn=conn, cursor=cursor)
            conn.commit()
            dados = [()]
    
        elif Btn == "listar":
            nome = request.form.get("CLASSICOINPUT")
            tempo = request.form.get("TEMPOINPUT")
            db.inserir_dados(conn=conn, cursor=cursor, nome=nome, tempo=tempo, tipo=tipo)
            conn.commit()
            dados = db.buscar_dados(cursor=cursor, tipo=tipo)
            
        conn.close()
    return render_template("classica.html", dados=dados)


if __name__ == "__main__":
    app.run(debug=True)