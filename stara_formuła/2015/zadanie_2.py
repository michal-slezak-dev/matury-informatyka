with open("slowa (4).txt", "r", encoding="UTF-8") as plik:
    slowa_binarne = []

    for line in plik:
        slowa_binarne.append(line.strip())

# print(slowa_binarne)

liczba_slow = 0

for slowo in slowa_binarne:
    bloki = 1
    for i in range(1, len(slowo)):
        if slowo[0] == '0' and slowo[i - 1] != slowo[i]:
            bloki += 1
    if bloki == 2:
        liczba_slow += 1

print(f'b) Słów składających się z 2 niepustych bloków jest:{liczba_slow}')

with open('wyniki4.txt', "a", encoding="UTF-8") as file:
    file.write("\n b) Słów składających się z 2 niepustych bloków jest: " + str(liczba_slow))
