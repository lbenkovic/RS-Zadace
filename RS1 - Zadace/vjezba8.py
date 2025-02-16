done = False
polje = []
while not done:
    user = input("Unesite broj (za prekid unesite 'done'): ")
    if (user == 'done'):

        done = True
    else:
        polje.append(int(user))

def filtriraj_parne(polje):
    filtrirano_polje = []
    for i in polje:
        if (i % 2 == 0):
            filtrirano_polje.append(i)
    return filtrirano_polje

print(filtriraj_parne(polje))