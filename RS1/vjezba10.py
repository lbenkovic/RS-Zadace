tekst = input("Unesite tekst: ")
tekst = tekst.split(" ")

def brojanje_riječi(tekst):
    rijecnik = {}
    for riječ in tekst:
        if (riječ in rijecnik):
            rijecnik[riječ] += 1
        else:
            rijecnik[riječ] = 1
    return rijecnik

print(brojanje_riječi(tekst))
        