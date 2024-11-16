rijecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

def obrni_rijecnik(rijecnik):
    pomocni = {}
    for key,value in rijecnik.items():
        pomocni[value] = key
    return pomocni
    
    
print(obrni_rijecnik(rijecnik))