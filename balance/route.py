from balance import app
from flask import render_template

@app.route("/")
def inicio():

#octener los movimentos
    datos = [ {"date": "fecha1", "time": "hora1", "concet": "c1", "type": "I", "mount": 1000},
              {"date": "fecha2", "time": "hora2", "concet": "c2", "type": "I55", "mount": 5},
              {"date": "fecha3", "time": "hora3", "concet": "c3", "type": "e22", "mount": 200},

            ]

 #ejecutar select fecha, hora, concet,
    return render_template("movimientos.html", movimientos=datos)