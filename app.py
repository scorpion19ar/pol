from flask import Flask, jsonify
from data_service import obtener_partidos

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde Flask en Render!'

@app.route('/datos')
def datos():
    datos_partidos = obtener_partidos()
    return jsonify(datos_partidos)

if __name__ == '__main__':
    app.run(debug=True)
