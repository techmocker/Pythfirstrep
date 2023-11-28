# Funktion für Addition
def addieren(a, b):
    return a + b

# Funktion für Subtraktion
def subtrahieren(a, b):
    return a - b

# Funktion für Multiplikation
def multiplizieren(a, b):
    return a * b

# Code
def rechnen():
    print("Rechner")
    
    operation = input("Welche berechnung willst du durchführen? (+/-/*): ")
    
    if operation not in ['+', '-', '*']:
        print("Bitte nimm eine gültige Methode.")
        return
    
    zahl1 = float(input("Gib die erste Zahl ein: "))
    zahl2 = float(input("Gib die zweite Zahl ein: "))

    if operation == '+':
        print(f"Das Ergebnis ist: {addieren(zahl1, zahl2)}")
    elif operation == '-':
        print(f"Das Ergebnis ist: {subtrahieren(zahl1, zahl2)}")
    elif operation == '*':
        print(f"Das Ergebnis ist: {multiplizieren(zahl1, zahl2)}")

# Funktion aufrufen
rechnen()
