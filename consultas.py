import sqlite3

con = sqlite3.connect()

cur = con.cursor()

cur.execute("""
                

            """

)

l = cur.fetchall()

print(l)

con.close
