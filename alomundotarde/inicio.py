from classes.matematica import Matematica
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return 'Olá, mundo!'


@app.route('/olamundo')
def mostar():
    return render_template('pagina.html')

@app.route('/calcularsoma')
def calcular():
    mat = Matematica(5,7)
    resposta = mat.somar()
    return render_template('calculo.html', resultado=resposta)

app.run() # não esquecer
