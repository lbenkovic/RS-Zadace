broj = 0
while broj < 5:
    broj +=2
    print(broj)

# ispis - 2 4 6 - u prvom koraku ispiše 2 jer je 0 prije ulaska u petlju, u drugom koraku je 2 te se ispise 4, u trecem koraku je 4 i ispise se 6 

broj = 0
while broj < 5:
    broj += 1
    print(broj)
    broj -= 1

# broj je uvijek = 0, poveca se za 1 i smanji u istom koraku

broj = 10
while broj > 0:
    broj -= 1
    print(broj)
    if broj < 5:
        broj += 2

# broj = 10, broj = 9, broj = 8, broj = 7, broj = 6, broj = 5, broj = 4 -> broj = 6, broj = 5, broj = 4 -> broj = 6 ...... beskonacna petlja 4/5