x = int(input("Gib eine Zahl an:"))
y = int(input("Gib eine zweite Zahl an:"))

def addiere(a, b):
    summe = a + b
    return summe, "gerade" if summe % 2 == 0 else "ungerade"

ergebnis, paritaet = addiere(x, y)
print(f"Ergebnis: {ergebnis}, Summe ist {paritaet}.")
