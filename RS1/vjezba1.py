# Vjezba 1
num1 = float(input("Unesite prvi broj: "))
num2 = float(input("Unesi drugi broj: "))
op = str(input("Unesi operator (+,-,*,/): "))


match op:
    case "+":
        res = num1 + num2
        print("Rezultat operacije ", num1, op, num2, " je ", res)
    case "-":
        res = num1 - num2
        print("Rezultat operacije ", num1, op, num2, " je ", res)
    case "*":
        res = num1 * num2
        print("Rezultat operacije ", num1, op, num2, " je ", res)
    case "/":
        if(num2 == 0):
            res = "Dijeljenje s nulom nije dozvoljeno!"
            print(res)
        else:
            res = num1 / num2
            print("Rezultat operacije ", num1, op, num2, " je ", res)
    case _:
        res = "Nepodržani operator!"
        print(res)
        