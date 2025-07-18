
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola desde Flask en Render!'

@app.route('/pronosticos')
def pronosticos():
    return jsonify([
        {"partido": "Godoy Cruz vs Sarmiento", "gana": "Godoy Cruz"},
        {"partido": "River Plate vs Instituto", "gana": "River Plate"},
        {"partido": "Boca Juniors vs Unión", "gana": "Boca Juniors"},
        {"partido": "Estudiantes vs Huracán", "gana": "Estudiantes"},
        {"partido": "Atlético Tucumán vs Central Córdoba", "gana": "Atlético Tucumán"},
        {"partido": "Newell's vs Banfield", "gana": "Newell's"},
        {"partido": "San Lorenzo vs Gimnasia", "gana": "San Lorenzo"},
        {"partido": "Lanús vs Rosario Central", "gana": "Lanús"},
        {"partido": "Vélez vs Platense", "gana": "Vélez"},
        {"partido": "Racing vs Belgrano", "gana": "Racing Club"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
