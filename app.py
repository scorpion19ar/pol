from flask import Flask, jsonify
from data_service import obtener_partidos

app = Flask(__name__)

@app.route('/')
def inicio():
    return "¡Hola desde Flask en Render!"

@app.route('/datos')
def datos():
    resultados = obtener_partidos()
    return jsonify(resultados)

