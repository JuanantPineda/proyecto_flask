from flask import Flask, render_template, abort, redirect
app = Flask(__name__)	

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

app.run("0.0.0.0",5000,debug=True)