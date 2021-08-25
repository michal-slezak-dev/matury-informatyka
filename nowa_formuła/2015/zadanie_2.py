with open("liczby_binarne.txt", "r") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())


podzielna_przez_2 = 0
podzielna_przez_8 = 0

for liczba in liczby:
    if liczba[-1] == '0' and liczba[-2] == '0' and liczba[-3] == '0':
        podzielna_przez_8 += 1
        podzielna_przez_2 += 1
    elif liczba[-1] == '0':
        podzielna_przez_2 += 1

print(podzielna_przez_2, ' ', podzielna_przez_8)

with open("wynik4.txt", "a", encoding="UTF-8") as plik:
    plik.write("b) " + str(podzielna_przez_2) + " " + str(podzielna_przez_8) + "\n")
