# Überprüfung des Alters
def alterspruefung(alter):
    if alter >= 18:
        return True
    else:
        return False

# Abfrage+Ausgabe
benutzer_alter = int(input("Wie alt bist du? "))
if alterspruefung(benutzer_alter):
    print("Tabakware genehmigt.")
else:
    print("Tabakware bitte zurück legen da du nicht Volljährig bist.")
