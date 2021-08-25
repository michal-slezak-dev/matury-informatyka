with open("liczby_binarne.txt", "r") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())

liczby_dziesietne = []

for liczba in liczby:
    liczby_dziesietne.append(int(liczba, base=2))


najwieksza_liczba_dziesietna = max(liczby_dziesietne)
najwieksza_liczba_binarna = bin(najwieksza_liczba_dziesietna)

najwieksza_liczba_binarna_string = str(najwieksza_liczba_binarna)

najwieksza_liczba_binarna_bez_0b = najwieksza_liczba_binarna_string.lstrip("0b")
# for i in range(1000):
#     if liczby[i] == najwieksza_liczba_binarna_bez_0b:
#         print(i + 1)

najmniejsza_liczba_dziesietna = min(liczby_dziesietne)
najmniejsza_liczba_binarna = bin(najmniejsza_liczba_dziesietna)

najmniejsza_liczba_binarna_string = str(najmniejsza_liczba_binarna)

najmniejsza_liczba_binarna_bez_0b = najmniejsza_liczba_binarna_string.lstrip("0b")
# for i in range(1000):
#     if liczby[i] == najmniejsza_liczba_binarna_bez_0b:
#         print(i + 1)

print("Wiersz dla maksimum: ", liczby.index(najwieksza_liczba_binarna_bez_0b) + 1)
print("Wiersz dla minimum: ", liczby.index(najmniejsza_liczba_binarna_bez_0b) + 1)

with open("wynik4.txt", "a", encoding="UTF-8") as plik:
    plik.write("c) " + "Wiersz dla maksimum: " + str(liczby.index(najwieksza_liczba_binarna_bez_0b) + 1) + "\n" + "Wiersz dla minimum: " + str(liczby.index(najmniejsza_liczba_binarna_bez_0b) + 1))
