from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

sorteos = {
    2255: 1,
    3748: 2,
    4567: 3
}

VALOR_PREMIO_TOTAL = 150_000_000
VALOR_BILLETE = 10_000
FECHA_EMISION = "12/06/2025"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado')
def resultado():
    boletos = {}
    for num_sorteo in sorteos.keys():
        boletos[num_sorteo] = [random.randint(1000, 9999) for _ in range(10)]

    ganadores = {}
    for num_sorteo, lista_boletos in boletos.items():
        min_boleto = min(lista_boletos)
        max_boleto = max(lista_boletos)
        ganador = random.randint(min_boleto, max_boleto)
        ganadores[num_sorteo] = ganador

    conteo_ganadores = {}
    for num_ganador in ganadores.values():
        conteo_ganadores[num_ganador] = conteo_ganadores.get(num_ganador, 0) + 1

    premios = {}
    for sorteo, num_ganador in ganadores.items():
        num_ganadores = conteo_ganadores[num_ganador]
        premios[sorteo] = VALOR_PREMIO_TOTAL // num_ganadores

    resultados = []
    for num_sorteo, num_ganador in ganadores.items():
        resultados.append({
            "sorteo": num_sorteo,
            "serie": sorteos[num_sorteo],
            "numero_ganador": num_ganador,
            "premio": premios[num_sorteo],
            "fecha": FECHA_EMISION,
            "valor_billete": VALOR_BILLETE
        })

    return render_template('resultado.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)