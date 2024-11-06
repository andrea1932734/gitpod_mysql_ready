import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS animali")
mycursor.execute("USE animali")
mycursor.execute("CREATE TABLE IF NOT EXISTS animali (nome_proprio VARCHAR(255), razza VARCHAR(255),id VARCHAR(255), peso INT, eta INT)")

sql = "INSERT INTO animali(nome_proprio, razza, id, peso, eta) VALUES (%s, %s, %s, %s, %s)"

val = [
    ('samuel', 'maiale', 'uno', 200, 19),
    ('luca', 'pollo', 'due', 10, 12),
    ('tommaso', 'toro', 'tre', 250, 15),
    ('andrea', 'cane', 'quattro', 16, 20),
    ('giovanni', 'cavallo', 'cinque', 400, 17)
]

# Utilizziamo executemany() per inserire più righe in una sola volta
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")