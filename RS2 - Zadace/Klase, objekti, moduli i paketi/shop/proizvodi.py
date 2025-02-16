class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} eur, Dostupna količina: {self.dostupna_kolicina}")

skladiste = [
    Proizvod("Pametni telefon", 1000, 15),
    Proizvod("Televizor", 4000, 5),
]

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    novi_proizvod = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi_proizvod)
