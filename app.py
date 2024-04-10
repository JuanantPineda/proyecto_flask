from flask import Flask, render_template, abort, redirect,request
app = Flask(__name__)	

import json
with open("estructura.json") as fichero:
    datos=json.load(fichero)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/listaepisodios',methods=["POST"])
def episodios():
    cadena=request.form.get("letra")

    episodios = []
    finalEpisodios = []

    for var in datos["_embedded"]["episodes"]:
        diccionario = {"nombre": var["name"], "puntuacion": var["rating"]["average"],"id": var["id"]}
        episodios.append(diccionario)

    for var in episodios:
        if var["nombre"].startswith(cadena):
            diccionario2 = {"nombre": var["nombre"], "puntuacion": var["puntuacion"], "id":var["id"]}
            finalEpisodios.append(diccionario2)

    return render_template("listaepisodios.html",finalEpisodios=finalEpisodios)

app.run("0.0.0.0",5000,debug=True)