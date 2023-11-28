# Wörterbuch von englischen zu deutsch
woerterbuch = {
    'hello': 'Hallo',
    'world': 'Welt',
    'cookie': 'Keks',
    # erweiterbar
}

# Nach Begriff fragen
suchbegriff = input("Gib einen Begriff ein: ").lower()  # Kleinschreibung falls der Begriff nicht übereinstimmt
if suchbegriff in woerterbuch:
    print(f"{suchbegriff.capitalize()} auf Deutsch bedeutet {woerterbuch[suchbegriff]}.")
else:
    print("Nicht im Wörterbuch gefunden.")