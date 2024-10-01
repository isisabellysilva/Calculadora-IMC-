from flask import Flask, render_template, request

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o cálculo do IMC
@app.route('/calcular', methods=['POST'])
def calcular():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        classificacao = 'Magreza'
    elif 18.5 <= imc < 24.9:
        classificacao = 'Peso normal'
    elif 25 <= imc < 29.9:
        classificacao = 'Sobrepeso'
    elif 30 <= imc < 39.9:
        classificacao = 'Obesidade'
    else:
        classificacao = 'Obesidade grave'
    
    return render_template('result.html', imc=round(imc, 1), classificacao=classificacao)
app.run(host='127.0.0.1', port=80, debug=True)
