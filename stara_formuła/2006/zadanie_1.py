with open("dane_2006.txt", "r", encoding="UTF-8") as plik:
    slowa = []

    for line in plik:
        slowa.append(line.strip())

# print(slowa)

# a) ilość słów występoujących więcej niż 1 raz
slowa_wystepujace_wiecej_niz_1_raz = 0
slownik_slow = {}

for slowo in slowa:
    slownik_slow.update({slowo: slowa.count(slowo)})

for slowo in slownik_slow:
    if slownik_slow[slowo] > 1:
        slowa_wystepujace_wiecej_niz_1_raz += 1

# print(slownik_slow)
print(f'Słów występujących więcej niż 1 raz jest: {slowa_wystepujace_wiecej_niz_1_raz}')

# b) dominanta
dominanta = slowa[0]
ilosc_wystapien = 1

for slowo in slowa:
    if slowa.count(slowo) > ilosc_wystapien:
        ilosc_wystapien = slowa.count(slowo)
        dominanta = slowo

print(f'Dominanta to: {dominanta}')

# c)Liczba wystąpień dominanty
print(f'Dominanta wystąpiła {ilosc_wystapien} razy.')

with open("wynik.txt", "w", encoding="UTF-8") as plik:
    plik.write(f'a) Słów występujących więcej niż 1 raz jest: {slowa_wystepujace_wiecej_niz_1_raz} \n')
    plik.write(f'Dominanta to: {dominanta} \n')
    plik.write(f'Dominanta wystąpiła {slowa.count(dominanta)} razy. \n \n')
