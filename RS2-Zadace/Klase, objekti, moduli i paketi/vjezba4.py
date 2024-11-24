from datetime import datetime

#1
class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")

auto = Automobil("Audi", "A4", 2008, 220000)

auto.ispis()
auto.starost()

#2
class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        print(f"{self.a} + {self.b} = {self.a + self.b}")

    def oduzimanje(self):
        print(f"{self.a} - {self.b} = {self.a - self.b}")

    def mnozenje(self):
        print(f"{self.a} * {self.b} = {self.a * self.b}")

    def dijeljenje(self):
        print(f"{self.a} / {self.b} = {(self.a / self.b):.2f}")
    
    def potenciranje(self):
        print(f"{self.a} ^ {self.b} = {self.a ** self.b}")
    
    def korijen(self):
        rezultat = self.b ** (1 / self.a)
        print(f"{self.a}-ti korijen od {self.b} = {rezultat:.2f}")

calc = Kalkulator(2,3)
calc.zbroj()
calc.oduzimanje()
calc.mnozenje()
calc.dijeljenje()
calc.potenciranje()
calc.korijen()

#3
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]
class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene
    
    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

student_objekti = [Student(x["ime"], x["prezime"], x["godine"], x["ocjene"]) for x in studenti]

najbolji_student = max(student_objekti, key=lambda s: s.prosjek())

print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}")
print(f"Prosjek ocjena: {najbolji_student.prosjek():.2f}")

#4
class Krug:
    def __init__(self, r):
        self.r = r
    
    def opseg(self):
        print(f"Opseg kruga: {((2 * self.r) * 3.14):.2f}")
    
    def povrsina(self):
        print(f"Površina kruga: {((self.r **2) * 3.14):.2f}")

krug = Krug(3)
krug.opseg()
krug.povrsina()

#5
class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"Povećana plaća radnika {radnik.ime}. Nova plaća: {radnik.placa}")


radnik1 = Radnik("Ivan", "Programer", 8000)
manager1 = Manager("Ana", "Voditelj", 12000, "IT")

radnik1.work() 
manager1.work()  

manager1.give_raise(radnik1, 2000)  
