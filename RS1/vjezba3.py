from random import randrange

num = randrange(1,100)

broj_je_pogoden = False
counter = 0

while not broj_je_pogoden:
    broj = int(input("Unesi broj: "))
    if (broj != num):
        print("Niste pogodili broj! Pokušajte ponovno!")
        counter += 1
    else:
        print("Bravo, pogodio si u ", counter, " pokušaja!")
        broj_je_pogoden = True;

