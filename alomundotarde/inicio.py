from classes.matematica import Matematica
from classes.timefut import Timefut
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

@app.route('/listatimes')
def listar_times():
    t1 = Timefut('Palmeiras',10)
    t2 = Timefut('Botafogo',10)
    t3 = Timefut('Flamengo',10)
    lista=[t1,t2,t3]
    return render_template('listatimes.html', times=lista)

app.run(debug=True) # não esquecer
