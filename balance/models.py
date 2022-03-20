import sqlite3

class ProcesaDatos:

    def recupera_datos(self):
        con = sqlite3.connect("datos/movimientos.db")
        cur = con.cursor()


        cur.execute("""
                        SELECT fecha, hora, concepto, es_ingreso, cantidad
                        FROM movimientos
                        ORDER BY fecha
                    """
        )

        return cur.fetchall()

    def modifica_datos(self, params):
        con = sqlite3.connect("datos/movimientos.db")
        cur = con.cursor()

        cur.execute("""
        INSERT INTO movimientos (fecha, hora, concepto, es_ingreso, cantidad)
                          values (?, ?, ?, ?, ?)
        """, params)

        con.commit()
       


