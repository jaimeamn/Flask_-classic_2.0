from balance import app
from flask import render_template, flash, request
from balance.models import ProcesaDatos
import sqlite3
from balance.forms import MovimientosForm


@app.route("/")
def inicio():

    data_manager = ProcesaDatos()
    try:
        datos = data_manager.recupera_datos()
        return render_template("movimientos.html", movimientos=datos)
    except sqlite3.Error as e:
        flash("Se ha producido un error en la base de datos. Inténtelo en unos instantes.")
        return render_template("movimientos.html", movimientos=[])


@app.route("/alta", methods=['GET', 'POST'])
def alta():
    form = MovimientosForm()
    if request.method == 'GET':
        return render_template("alta.html", formulario=form)
    else:   
        # validar 
        # pasando por ahora
        # recuperar los datos de form y pasarselos al modelo para que los grabe
         fecha = form.fecha.data.tostring()
         hora = form.hora.data.tostring()
         concepto = form.concepto.data
         es_ingreso = int(form.es_ingreso.data)
         cantidad = form.cantidad.data

        
         query = """
         INSERT INTO movimientos (fecha, hora, concepto, es_ingreso, cantidad)
                           values (?, ?, ?, ?, ?)
         """
         

         cur.execute(query, (fecha, hora, concepto, es_ingreso, cantidad))
        