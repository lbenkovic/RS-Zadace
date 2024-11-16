lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def grupiraj_po_paritetu(lista):
    rijecnik = {'parni': [], 'neparni': []}
    for broj in lista:
        if (broj %2 == 0):
            rijecnik['parni'].append(broj)
        else:
            rijecnik['neparni'].append(broj)
    return rijecnik

print(grupiraj_po_paritetu(lista))
        