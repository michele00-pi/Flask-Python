from flask import Flask, render_template, request

app = Flask(__name__)

lista_brasil = []
lista_gringo = []

@app.route("/") #Pagina inicial

def main():
    return render_template("main.html")

@app.route("/brasileira", methods=["POST", "GET"]) #Pagina das musicas brasileiras

def page_brasileira():
        
    if request.method == 'POST':

        musica_brasileira = request.form.get("BRASILINPUT")
        lista_brasil.append(musica_brasileira)

    if request.method == 'GET':

        lista_brasil.clear()

    return render_template("brasileira.html", lista_brasil=lista_brasil)


@app.route("/estrangeira", methods=["POST", "GET"]) #Pagina das musicas estrangeiras

def page_estrangeira():

    if request.method == 'POST':

        nome = request.form.get("ESTRANGEIROINPUT")
        tempo = request.form.get("TEMPOINPUT")

        lista_gringo.append(
            {
            "Nome": nome,
            "Tempo": tempo
            }
        )

    if request.method == 'GET':
        
        lista_gringo.clear()
    
    return render_template("estrangeira.html", lista_gringo=lista_gringo)

@app.route("/classica") #Pagina das musicas classicas

def page_classica():
    return render_template("classica.html")

if __name__ == "__main__":
    app.run(debug=True)