from balance import app
from flask import render_template, flash, request, redirect, url_for
from balance.models import ProcesaDatos
import sqlite3
from balance.forms import MovimientosForm
from datetime import date, time

ruta_db = app.config['RUTA_BBDD']
data_manager = ProcesaDatos(ruta_db)


@app.route("/")
def inicio():

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
        if form.validate():
            # recuperar los datos de form y pasarselos al modelo para que los grabe
            fecha = str(form.fecha.data)
            hora = str(form.hora.data)
            concepto = form.concepto.data
            es_ingreso = int(form.es_ingreso.data)
            cantidad = form.cantidad.data

            try:    
                data_manager.modifica_datos((fecha, hora, concepto, es_ingreso, cantidad))
                return redirect(url_for("inicio"))
            except sqlite3.Error as e:
                flash("Se ha producido un error en la base de datos. Inténtelo en unos instantes.")
                return render_template("alta.html", formulario=form)
        else:
            return render_template("alta.html", formulario=form)

@app.route("/modifica/<int:id>", methods=['GET', 'POST'])
def modificar(id):
    if request.method == 'GET':
        #1.consultar el movimiento id

        try:
            movimientos = data_manager.consulta_id(id)
            if len(movimientos) == 0:
                flash(f"no existe el movimiento {id}")
                return redirect(url_for("inicio"))

            movimiento = movimientos[0]
            movimiento['fecha'] = date.fromisoformat(movimiento['fecha'])
            movimiento['hora'] = time.fromisoformat(movimiento['hora'])

            form = MovimientosForm(data=movimiento)
            return render_template("modifica.html", formulario=form, id=id)

            #3.Renderizar el formulario y devolverlo al navegador
        except sqlite3.Error as e:
            flash("Se ha producido un error en la base de datos. Inténtelo en unos instantes.")
            form = MovimientosForm()
            return render_template("modifica.html", formulario=form, id=id)


    else:
        form = MovimientosForm()
        #1. validar
        if form.validate():
            params = (str(form.fecha.data), str(form.hora.data), form.concepto.data, 
                      form.es_ingreso.data, form.cantidad.data, id)
            try:
                data_manager.update_datos(params)
                return redirect(url_for("inicio"))
            except sqlite3.Error as e:
                flash("Se ha producido un error en la base de datos. Inténtelo en unos instantes.")
                return render_template("modifica.html", formulario=form, id=id)
        else:
            return render_template("modifica.html", formulario=form, id=id)

        
        #2. Insertar
        #3. redirect a /

        