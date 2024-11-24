from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        detalji = ", ".join([f"{pro['naziv']} x {pro['kolicina']}" for pro in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {detalji}, Ukupna cijena: {self.ukupna_cijena} eur")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list) or not naruceni_proizvodi:
        print("Narudžba mora biti lista i ne smije biti prazna!")
        return None
    if not all(isinstance(p, dict) for p in naruceni_proizvodi):
        print("Svaki proizvod u narudžbi mora biti rječnik!")
        return None
    if not all("naziv" in p and "kolicina" in p for p in naruceni_proizvodi):
        print("Svaki proizvod mora sadržavati ključeve 'naziv' i 'kolicina'!")
        return None

    ukupna_cijena = 0
    finalna_narudzba = []

    for proizvod in naruceni_proizvodi:
        naziv = proizvod["naziv"]
        kolicina = proizvod["kolicina"]
        
        skladisni_proizvod = next((p for p in skladiste if p.naziv == naziv), None)
        if not skladisni_proizvod or skladisni_proizvod.dostupna_kolicina < kolicina:
            print(f"Proizvod {naziv} nije dostupan ili nema dovoljno na stanju!")
            return None
        
        skladisni_proizvod.dostupna_kolicina -= kolicina
        ukupna_cijena += skladisni_proizvod.cijena * kolicina
        finalna_narudzba.append({"naziv": naziv, "kolicina": kolicina})

    narudzba = Narudzba(finalna_narudzba, ukupna_cijena)
    narudzbe.append(narudzba)
    return narudzba
