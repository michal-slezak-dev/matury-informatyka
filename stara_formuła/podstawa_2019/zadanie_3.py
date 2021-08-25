with open("dane_2019.txt", "r") as plik:
    lista_danych = []
    for line in plik:
        lista_danych.append(line.replace("\n", ""))

poprawne = []
ile = 0
bledne_numery = []
for pesel in lista_danych:
    if (
        1 * int(pesel[0])
        + 3 * int(pesel[1])
        + 7 * int(pesel[2])
        + 9 * int(pesel[3])
        + 1 * int(pesel[4])
        + 3 * int(pesel[5])
        + 7 * int(pesel[6])
        + 9 * int(pesel[7])
        + 1 * int(pesel[8])
        + 3 * int(pesel[9])
        + int(pesel[10])
    ) % 10 != 0:
        bledne_numery.append(pesel)
    else:
        poprawne.append(pesel)

print("Błędne numery PESEL to: \n")
for numer in bledne_numery:
    print(numer)

with open("odpowiedziPESEL.txt", "a", encoding="UTF-8") as plik:
    plik.write("c) Błędne numery PESEL to: \n")
    for numer in bledne_numery:
        plik.write(numer)
