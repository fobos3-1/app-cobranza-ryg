from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint 1: Cargar datos iniciales
data_temporal = {}  # almacenamiento simulado

@app.route('/cargar_datos', methods=['POST'])
def cargar_datos():
    data = request.get_json()
    data_temporal['carga'] = data
    return jsonify({"status": "ok", "mensaje": "Datos cargados exitosamente."})

# Endpoint 2: Subir movimientos del día
@app.route('/subir_movimientos', methods=['POST'])
def subir_movimientos():
    movimientos = request.get_json()
    data_temporal['movimientos'] = movimientos
    return jsonify({"status": "ok", "mensaje": "Movimientos registrados."})

# Endpoint 3: Resumen del día
@app.route('/resumen_dia', methods=['GET'])
def resumen_dia():
    resumen = {
        "monto_tickets": 10234,
        "cobros_extra": 534,
        "cobros_faltantes": 189,
        "productos_descontados": 320
    }
    return jsonify(resumen)

# Endpoint 4: Validar código de crédito
@app.route('/validar_codigo', methods=['POST'])
def validar_codigo():
    datos = request.get_json()
    codigo_ingresado = datos.get("codigo")
    # Aquí podrías consultar una BD real
    if codigo_ingresado == "12345":
        return jsonify({"valido": True})
    return jsonify({"valido": False})

# Endpoint 5: Entregar tarjeta a cliente
@app.route('/entregar_tarjeta', methods=['POST'])
def entregar_tarjeta():
    datos = request.get_json()
    cliente = datos.get("cliente")
    tarjeta = datos.get("id_tarjeta")
    data_temporal['tarjeta_' + str(cliente)] = tarjeta
    return jsonify({"status": "ok", "mensaje": f"Tarjeta {tarjeta} asignada al cliente {cliente}"})

# Endpoint 6: Saludar, chingaos
@app.route("/saludo")
def saludo():
    return "¡Hola, mundo!"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
