from balance import app
from flask import render_template
import sqlite3

@app.route("/")
def inicio():

#octener los movimentos
    datos = [ {"date": "fecha1", "time": "hora1", "concet": "c1", "type": "I", "mount": 1000},
              {"date": "fecha2", "time": "hora2", "concet": "c2", "type": "I55", "mount": 5},
              {"date": "fecha3", "time": "hora3", "concet": "c3", "type": "e22", "mount": 200},

            ]

 #ejecutar select fecha, hora, concet,
    con = sqlite3.connect("data/movimientos.sqlite")
    cur = con.cursor()

    cur.execute(""" 
                    SELECT fecha, hora, concepto, es_ingreso, cantidad
                        FROM movimientos
                     ORDER BY fecha
                """
    
    )

    datos =[]
    dato = cur.fetchone()
    while dato:
        dato = list(dato)
        if dato[3] ==1:
            dato[3] = "Ingreso"
        else:
            dato[3] = "Gasto"
        
        #datos[3] = "Ingreso" if datos[3] else "Gasto"

        datos.append(dato)
        dato = cur.fetchone()

    return render_template("movimientos.html", movimientos=datos)