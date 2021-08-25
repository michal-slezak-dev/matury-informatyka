with open("liczby_binarne.txt", "r") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())

liczby_dziesietne = []

for liczba in liczby:
    liczby_dziesietne.append(int(liczba, base=2))


najwieksza_liczba_dziesietna = max(liczby_dziesietne)
najwieksza_liczba_binarna = str(bin(najwieksza_liczba_dziesietna)).lstrip("0b")

# for i in range(1000):
#     if liczby[i] == najwieksza_liczba_binarna:
#         print(i + 1)

najmniejsza_liczba_dziesietna = min(liczby_dziesietne)
najmniejsza_liczba_binarna = str(bin(najmniejsza_liczba_dziesietna)).lstrip("0b")

# for i in range(1000):
#     if liczby[i] == najmniejsza_liczba_binarna:
#         print(i + 1)

print("Wiersz dla maksimum: ", liczby.index(najwieksza_liczba_binarna) + 1)
print("Wiersz dla minimum: ", liczby.index(najmniejsza_liczba_binarna) + 1)

with open("wynik4.txt", "a", encoding="UTF-8") as plik:
    plik.write("c) " + "Wiersz dla maksimum: " + str(liczby.index(najwieksza_liczba_binarna) + 1) + "\n" + "Wiersz dla minimum: " + str(liczby.index(najmniejsza_liczba_binarna) + 1))
