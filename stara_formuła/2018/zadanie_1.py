with open("slowa_2018.txt", "r", encoding="UTF-8") as plik:
    slowa = []
    for line in plik:
        slowa.append(line.strip())


slowa1 = []
koniec_litera_A = 0

for slowo in slowa:
    slowa1.append(slowo.split())

for slowo1, slowo2 in slowa1:
    if slowo1[-1] == "A":
        koniec_litera_A += 1
    if slowo2[-1] == "A":
        koniec_litera_A += 1

print("Słów kończących się na 'A' jest: ", koniec_litera_A)

with open("wyniki6.txt", "w", encoding="UTF-8") as plik:
    plik.write("a) Słów kończących się na 'A' jest: " + str(koniec_litera_A) + "\n")
