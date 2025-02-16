vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

def count_vowels_consonants(tekst):
    rijecnik = {'vowels': 0, 'consonants':0}
    for i in tekst:
        if i in vowels:
            rijecnik['vowels'] += 1
        elif i in consonants:
            rijecnik['consonants'] += 1
    return rijecnik

print(count_vowels_consonants(tekst))
# {'vowels': 30, 'consonants': 48}