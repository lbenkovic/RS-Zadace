for i in range(1, 2):
    print(i)

# nema smisla jer je je range od 1 - 2, tj for petlja ide do n-1, gdje je n = 1, sto znaci da ce se odradit jednom i ispisati samo 1


for i in range(1, 10, 2):
    print(i)

# print - 1, 3, 5, 7, 9 - range od 1 do n - 1, sa korakom 2, odnosno i se povecava za +2


for i in range(10, 1, -1):
    print(i)

#print - 10, 9, 8, 7, 6, 5, 4, 3, 2 - petlja ide od 10 do n + 1 jer je "smjer" petlje obrnut