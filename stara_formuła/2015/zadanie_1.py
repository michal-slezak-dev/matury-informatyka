with open("slowa (4).txt", "r", encoding="UTF-8") as plik:
    slowa_binarne = []

    for line in plik:
        slowa_binarne.append(line.strip())

# print(slowa_binarne)

liczba_slow = 0

for slowo in slowa_binarne:
    zera = 0
    jedynki = 0

    for litera in slowo:
        if litera == '0':
            zera += 1
        else:
            jedynki += 1
    if zera > jedynki:
        liczba_slow += 1

print("a) Słów, w których liczba 0 jest większa od liczby jedynek jest: " + str(liczba_slow))



with open('wyniki4.txt', "w", encoding="UTF-8") as file:
    file.write("a) Słów, w których liczba 0 jest większa od liczby jedynek jest: " + str(liczba_slow))
