#1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def prvi_i_zadnji(list):
    return list[0], list[len(list)-1]

print(prvi_i_zadnji(lista)) # (1, 10)

#2
lista = [5, 10, 20, 50, 100, 11, 250, 50, 80]

def maks_i_min(list):
    max = list[0]
    min = list[0]
    for i in list:
        if (i > max):
            max = i
        elif (i < min):
            min = i
    return max, min

print(maks_i_min(lista)) # (250, 5)

#3
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}

def presjek(skup1, skup2):
    return skup1.intersection(skup2)

print(presjek(skup_1, skup_2)) # {4, 5}