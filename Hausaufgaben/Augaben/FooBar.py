# Wort fragen
word = input("Worteingabe: ")

# Zahl fragen
user_input = input("Zahleingabe: ")

# Checken ob es eine Zahl ist
try:
    num = int(user_input)
except ValueError:
    print("Ungültig. Keine Zahl erkannt.")
    exit()

# Funktion zum Überprüfen der Zahl
def check_number(number):
    output = ""

    if number % 7 == 0:
        output += "Foo"
    if number % 11 == 0:
        output += "Bar"
    if number % 77 == 0:
        output += "s"

    return output if output else number

# Ergebnis ausgeben
result = check_number(num)
print(f"Ergebnis für die Zahl {num} mit dem Wort '{word}': {result}")

#Schließen
input("Drücke Enter zum schließen.")