def najpopularniejsza(lista):
    liczba_wystapien = {}

    for element in lista:
        liczba_wystapien.update({element: lista.count(element)})

    najwieksza_liczba_wystapien = max(liczba_wystapien.values())

    dominanty = []

    for klucz in liczba_wystapien:
        if liczba_wystapien[klucz] == najwieksza_liczba_wystapien:
            dominanty.append(klucz)
    return dominanty

### PLIK dane5-1.txt ###
with open("dane5-1.txt", "r", encoding="UTF-8") as plik:
    liczby_1 = []

    for line in plik:
        liczby_1.append(int(line.strip()))
# print(liczby_1)

print("Najpopularniejsze liczby/-a w pliku dane5-1.txt: ", end="")
for dominanta in najpopularniejsza(liczby_1):
    print(dominanta, end=", ")

### PLIK dane5-2.txt ###
with open("dane5-2.txt", "r", encoding="UTF-8") as plik:
    liczby_2 = []

    for line in plik:
        liczby_2.append(int(line.strip()))
# print(liczby_2)

print("\nNajpopularniejsze liczby/-a w pliku dane5-2.txt: ", end="")
for dominanta in najpopularniejsza(liczby_2):
    print(dominanta, end=", ")

### PLIK dane5-3.txt ###
with open("dane5-3.txt", "r", encoding="UTF-8") as plik:
    liczby_3 = []

    for line in plik:
        liczby_3.append(int(line.strip()))
# print(liczby_3)

print("\nNajpopularniejsze liczby/-a w pliku dane5-3.txt: ", end="")
for dominanta in najpopularniejsza(liczby_3):
    print(dominanta, end=", ")
