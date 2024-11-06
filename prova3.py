import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali"
)

def inserisci_animali(nome, razza, peso, eta):
    mycursor = mydb.cursor()
    
    mycursor.execute('''
    INSERT INTO animali (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)
    ''', (nome, razza, peso, eta))
    
    mydb.commit()
    mydb.close()
  

def verifica_input(valore):
    try:
        return int(valore)
    except ValueError:
        print("Errore: inserisci un numero intero.")
        return None

def chiedi_inserimenti():
    for _ in range(5):
        nome = input("Inserisci il nome dell'animale: ")
        razza = input("Inserisci la razza dell'animale: ")
        
        peso = None
        while peso is None:
            peso_input = input("Inserisci il peso dell'animale (in kg): ")
            peso = verifica_input(peso_input)
        
        eta = None
        while eta is None:
            eta_input = input("Inserisci l'età dell'animale (in anni): ")
            eta = verifica_input(eta_input)
        
        inserisci_animali(nome, razza, peso, eta)

if __name__ == '__main__':
    chiedi_inserimenti()