from collections import Counter

with open("slowa (4).txt", "r", encoding="UTF-8") as plik:
    slowa_binarne = []

    for line in plik:
        slowa_binarne.append(line.strip())

# print(slowa_binarne)

liczba_slow = 0

for slowo in slowa_binarne:
    if Counter(slowo)['0'] > Counter(slowo)['1']:
        liczba_slow += 1
print("a) Słów, w których liczba 0 jest większa od liczby jedynek jest: " + str(liczba_slow))
