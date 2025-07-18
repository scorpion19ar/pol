from flask import Flask, jsonify
from data_service import obtener_resultados_historicos

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola desde Flask en Render!"

@app.route('/historicos')
def historicos():
    df = obtener_resultados_historicos()
    return jsonify(df.to_dict(orient='records'))
