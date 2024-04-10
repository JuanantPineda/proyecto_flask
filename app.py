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

    for var in datos["_embedded"]["episodes"]:
        episodios.append(var["name"])

    for var in episodios:
        if var.startswith(cadena):
            print(var)
    return render_template("listaepisodios.html")

app.run("0.0.0.0",5000,debug=True)