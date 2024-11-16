def provjera_lozinke(lozinka):
    upper = 0
    number = 0
    forbiden = ('lozinka', 'password')
    for i in lozinka:
        if (i.isupper()):
            upper += 1
        if (i.isdigit()):
            number += 1
    if (len(lozinka) < 8 or len(lozinka) > 15):
        return "Lozinka mora sadržavati između 8 i 15 znakova."
    elif (upper == 0 or number == 0 ):
        return "Lozinka mora sadržavati barem jedno veliko slovo i jedan broj."
    elif (forbiden[0] in lozinka.lower() or forbiden[1] in lozinka.lower()):
        return "Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'"
    return "Lozinka je jaka!"

user = input("Unesi lozinku: ")

print(provjera_lozinke(user))