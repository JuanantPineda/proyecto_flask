from flask import Flask, render_template, abort, redirect,request
app = Flask(__name__)	

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/episodios',methods=["POST"])
def episodios():
    caracter=request.form.get("letra")
    return render_template("episodios.html")

app.run("0.0.0.0",5000,debug=True)