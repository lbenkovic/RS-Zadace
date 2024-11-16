done = False
polje = []
while not done:
    user = input("Unesite broj (za prekid unesite 'done'): ")
    if (user == 'done'):
        done = True
    else:
        polje.append(int(user))

def ukloni_duplikate(lista):
    polje2 = []
    for i in lista:
        if (i not in polje2):
            polje2.append(i)
    return polje2

print(ukloni_duplikate(polje))