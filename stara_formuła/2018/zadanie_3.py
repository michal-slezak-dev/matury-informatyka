with open("slowa_2018.txt", "r", encoding="UTF-8") as plik:
    slowa = []
    for line in plik:
        slowa.append(line.strip())


slowa1 = []
liczba_wierszy = 0

for slowo in slowa:
    slowa1.append(slowo.split())

for slowo1, slowo2 in slowa1:
    slowo1 = "".join(sorted(slowo1))
    slowo2 = "".join(sorted(slowo2))
    if slowo1 == slowo2:
        liczba_wierszy += 1

print("c) Liczba wierszy zawierających parę słów, gdzie jedno słowo jest anagramem drugiego:", liczba_wierszy)

with open("wyniki6.txt", "a", encoding="UTF-8") as plik:
    plik.write("c) Liczba wierszy zawierających parę słów, gdzie jedno słowo jest anagramem drugiego: " + str(liczba_wierszy) + "\n")
