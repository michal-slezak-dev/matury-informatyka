def czy_palindrom(slowo):
    #reversed_string = "".join(reversed(slowo))

    if slowo == "".join(reversed(slowo)):
        return True
    return False

with open("dane_2006.txt", "r", encoding="UTF-8") as plik:
    slowa = []

    for line in plik:
        slowa.append(line.strip())

# print(slowa)

ilosc_palindromow = 0

for slowo in slowa:
    if czy_palindrom(slowo):
        ilosc_palindromow += 1

print(f'Palindromów jest: {ilosc_palindromow}')

with open("wynik.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'c) Palindromów jest: {ilosc_palindromow}\n')
