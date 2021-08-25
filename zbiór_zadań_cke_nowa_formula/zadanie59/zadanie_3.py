# Ta funkcja zwraca na pierwszy iloczyn cyfr danej liczby
def iloczyn(liczba):
    iloczyn = 1
    for cyfra in str(liczba):
        iloczyn *= int(cyfra)
    return str(iloczyn)

# Ta funkcja zwraca nam moc danej liczby, pętla wykonuje się dopóki długość iloczynu cyfr nie jest równa 1
# jeśli jest równa 1 to pętla się kończy, w pętli mamy zmienną nowy_iloczyn, który oiblicza iloczyn cyfr pierwszego iloczynu
# dla liczby 678 pierwszy iloczyn to 336, więc w pętli jest sprawdzana najpierw długość liczby (jako napis) 336, jest ona równa 3, więc
# wywołujemy funkcję iloczyn, kltóra obliczy teraz iloczyn cyfr liczby 336 itd.
# za każdym obrotem pętli do zmiennej k, która reprezentuje moc dodajemy 1, na koniec zwracamy k + 1, ponieważ trzeba pamiętać o tym, że "pierwszy obrót pętli"
# wykonaliśmy w funkcji iloczyn, dlatego + 1
def moc(iloczynek_liczba):
    k = 0
    while len(iloczynek_liczba) != 1:
        nowy_iloczyn = iloczyn(iloczynek_liczba)
        iloczynek_liczba = nowy_iloczyn
        k += 1
    return k + 1

with open("liczby (2).txt", "r") as plik:
    liczby = []

    for line in plik:
        liczby.append(int(line.strip()))
# print(liczby)
# print(moc(iloczyn(1991)))

# Tutaj będziemy przechowywać moce liczb z listy liczby
moce = []

# Tutaj będziemy przechowywać liczby o mocy 1
moc_1 = []

# Tutaj w pętli do listy moce dodajemy moc danej liczby, a do listy moce_1 dodajemy liczby o mocy 1
for liczba in liczby:
    moce.append(moc(iloczyn(liczba)))
    if moc(iloczyn(liczba)) == 1:
        moc_1.append(liczba)
# print(moce)
# print(moc_1)

# Wyłaniamy maksymalną i minimalną liczbę o mocy 1
max_moc_1 = max(moc_1)
min_moc_1 = min(moc_1)

# Tutaj będzie słownik z ilością liczb o mocy od 1 do 8
moce_1_8 = {}

# Tutaj do słownika do kluczy dodajemy i, które jest od 1 do 8(... in range(1, n), range zawsze wykonuje się do n - 1, więc jak chcemy, żeby działała do 8 to trzeba dać 9)
# no i w końcu dodajemy do słownika i oraz liczbę wystąpień i, i to jest moc
for i in range(1, 9):
    for moc in moce:
        moce_1_8.update({i: moce.count(i)})
# print(moce_1_8)

# Wypisujemy
print(f'Ilość liczb o mocy od 1 do 8: \n')
for moc in moce_1_8:
    print(str(moc) + ": " + str(moce_1_8[moc]))

print(f'Najmniejsza  liczba o mocy 1: {min_moc_1}')
print(f'Największa  liczba o mocy 1: {max_moc_1}')


with open("wyniki_liczby.txt", "a", encoding="UTF-8") as plik:
    plik.write("Zadanie 59.3\n")
    plik.write(f'Ilość liczb o mocy od 1 do 8: \n')

    for moc in moce_1_8:
        plik.write(str(moc) + ": " + str(moce_1_8[moc]) + "\n")

    plik.write(f'Najmniejsza  liczba o mocy 1: {min_moc_1}\n')
    plik.write(f'Największa  liczba o mocy 1: {max_moc_1}')
