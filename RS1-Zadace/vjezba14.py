#1
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

print(isPrime(7)) # True
print(isPrime(10)) # False

#2
def primes_in_range(start, end):
    list = []
    for num in range(start, end):
        if isPrime(num):
            list.append(num)
    return list

print(primes_in_range(1, 10)) # [2, 3, 5, 7]
