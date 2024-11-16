godina = int(input("Unesi godinu: "))

def checkLeapYear(godina):
    if (godina % 4 == 0):
        if (godina % 100 == 0):
            print("Godina ", godina, " nije prijestupna!")
        else:
            print("Godina ", godina, " je prijestupna!")
    elif (godina % 400 == 0):
        print("Godina ", godina, " je prijestupna!")
    else: 
        print("Godina", godina, " nije prijestupna!")

checkLeapYear(godina)