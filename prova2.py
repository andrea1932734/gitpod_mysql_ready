import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS animali")
mycursor.execute("USE animali")

mycursor.execute("SELECT * FROM animali")

myresult = mycursor.fetchone()

print(myresult)