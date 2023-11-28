class Tiere:
    def __init__(self, herkunft, durchschnittsalter, name, hauptnahrung, ist_bedroht, ist_vegetarier):
        self.herkunft = herkunft
        self.durchschnittsalter = durchschnittsalter
        self.name = name
        self.hauptnahrung = hauptnahrung
        self.ist_bedroht = ist_bedroht
        self.ist_vegetarier = ist_vegetarier

    def zeige_infos(self):
        print("Tier:", self.name)
        print("Herkunft:", self.herkunft)
        print("Durchschnittsalter:", self.durchschnittsalter, "Jahre")
        print("Hauptnahrung:", self.hauptnahrung)
        print("Ist bedroht:", "Ja" if self.ist_bedroht else "Nein")
        print("Ist vegetarier:", "Ja" if self.ist_vegetarier else "Nein")

    def ernährungs_infos(self):
        print("Tier:", self.name)
        print("Hauptnahrung:", self.hauptnahrung)
        print("Ist vegetarier:", "Ja" if self.ist_vegetarier else "Nein")

# Tiere
tier1 = Tiere("Afrika", 15, "Löwe", "Fleisch", False, False)
tier2 = Tiere("Australien", 8, "Känguru", "Pflanzen", False, True)
tier3 = Tiere("Asien", 25, "Elefant", "Pflanzen", True, True)
tier4 = Tiere("Nordamerika", 10, "Bär", "Fisch", False, False)
tier5 = Tiere("Antarktis", 70, "Pinguin", "Fisch", False, False)
tier6 = Tiere("Südamerika", 5, "Ameisenbär", "Insekten", True, False)
tier7 = Tiere("Europa", 12, "Fuchs", "Kleintiere", False, False)
tier8 = Tiere("Ozeanien", 30, "Koala", "Eukalyptusblätter", False, True)
tier9 = Tiere("Afrika", 20, "Giraffe", "Blätter", False, True)
tier10 = Tiere("Asien", 18, "Tiger", "Fleisch", True, False)

# Infos für alle Tiere
print("Allgemeine Infos für alle Tiere:")
tier1.zeige_infos()
print("\n")
tier2.zeige_infos()
print("\n")
tier3.zeige_infos()
print("\n")
tier4.zeige_infos()
print("\n")
tier5.zeige_infos()
print("\n")
tier6.zeige_infos()
print("\n")
tier7.zeige_infos()
print("\n")
tier8.zeige_infos()
print("\n")
tier9.zeige_infos()
print("\n")
tier10.zeige_infos()
