from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola mundo desde Flask!"

@app.route('/saludo')
def saludo():
    return jsonify({"mensaje": "Hola, este es un endpoint de prueba."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
