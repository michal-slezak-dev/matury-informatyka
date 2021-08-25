def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    return False

with open("dane_2006.txt", "r", encoding="UTF-8") as plik:
    slowa = []

    for line in plik:
        slowa.append(line.strip())

# print(slowa)

liczby_szesnastkowe = []

for slowo in slowa:
    liczby_szesnastkowe.append(int(slowo, 16))

# print(liczby_szesnastkowe)

ilosc_liczb_parzystych = 0

for liczba in liczby_szesnastkowe:
    if czy_parzysta(liczba):
        ilosc_liczb_parzystych += 1

print(f' W pliku "dane.txt" są {ilosc_liczb_parzystych} liczby parzyste')

with open("wynik.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'b) W pliku "dane.txt" sa {ilosc_liczb_parzystych} liczby parzyste \n \n')
