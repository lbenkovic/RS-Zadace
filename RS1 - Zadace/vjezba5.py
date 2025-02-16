num = int(input("Unesite broj: "))

#for petlja
res = 1
for i in range(1, num + 1):
    res *= i
print(res)

# while petlja

res = 1
i = 1;
while i <= num:
    res *= i 
    i += 1

print(res)