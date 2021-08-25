with open("slowa_2018.txt", "r", encoding="UTF-8") as plik:
    slowa = []
    for line in plik:
        slowa.append(line.split())

ile_wierszy = 0

for slowo1, slowo2 in slowa:
    if slowo1 in slowo2:
        ile_wierszy += 1

print("b) Liczba wierszy, gdzie pierwsze słowo zawiera się w drugim: ", ile_wierszy)


with open("wyniki6.txt", "a", encoding="UTF-8") as plik:
    plik.write("b) Liczba wierszy, gdzie pierwsze słowo zawiera się w drugim: " + str(ile_wierszy) + "\n")
