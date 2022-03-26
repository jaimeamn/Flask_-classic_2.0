from balance import app
from flask import jsonify
import sqlite3

from balance.models import ProcesaDatos

ruta_db = app.config['RUTA_BBDD']
data_manager = ProcesaDatos(ruta_db)

@app.route("/api/v01/todos")
def todos():
    datos = data_manager.recupera_datos()
    return jsonify(datos)