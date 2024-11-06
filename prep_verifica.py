import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)


mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS verifica")
mycursor.execute("USE verifica")
mycursor.execute("CREATE TABLE  IF NOT EXISTS customers  (name VARCHAR(255), surname VARCHAR(255))")


sql = "INSERT INTO customers (name, surname) VALUES (%s, %s)"
val = [
  ('andrea', 'caro'),
  ('luca', 'mina'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

