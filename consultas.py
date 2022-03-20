import sqlite3

con = sqlite3.connect()

cur = con.cursor()

cur.execute("""
                select fecha, hora, concepto, es_ingreso, cantidad
                  from movimientos
                 order by fecha
            """
)

l = cur.fetchall()

print(l)

con.close
