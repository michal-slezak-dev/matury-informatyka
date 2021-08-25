def czy_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

with open("NAPISY_2014.TXT", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

# print(napisy)

ile_napisow = 0

for napis in napisy:
    suma = 0
    for litera in napis:
        suma += ord(litera)
    if czy_pierwsza(suma):
        ile_napisow += 1

print(ile_napisow)

with open("ZADANIE5.TXT", "w", encoding="UTF-8") as plik:
    plik.write(f'a) Napisów pierwszych jest: {ile_napisow}\n\n')
