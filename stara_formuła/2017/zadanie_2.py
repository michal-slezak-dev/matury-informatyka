def czy_nie_poprawne(napis):
    for i in range(4, len(napis) + 1, 4):
        napisDoKonwersji = napis[i - 4 : i]
        liczba = int(napisDoKonwersji, 2)
        if liczba > 9:
            return True
    return False


with open("binarne.txt", "r", encoding="UTF-8") as file:
    napisy_binarne = []

    for line in file:
        napisy_binarne.append(line.strip())

# print(napisy_binarne)

poprawne = 0
niepoprawne = 0

# 1 sposób
dlugosci_niepoprawnych_napisow = []

# 2 sposób
# dlugosci_niepoprawnych_napisow = {}

for napis in napisy_binarne:
    if czy_nie_poprawne(napis):
        dlugosci_niepoprawnych_napisow.append(len(napis))
        # dlugosci_niepoprawnych_napisow.update({napis: len(napis)})

        niepoprawne += 1
    else:
        poprawne += 1

minDlugosc = min(dlugosci_niepoprawnych_napisow)
# minDlugosc = min(dlugosci_niepoprawnych_napisow.values())

print(f"b) Niepoprawnych napisów jest {niepoprawne}\nNajmniejsza długość niepoprawnego napisu to: {minDlugosc}")

with open("zadanie4.txt", "a", encoding="UTF-8") as file:
    file.write(f"b) Niepoprawnych napisów jest {niepoprawne}\nNajmniejsza długość niepoprawnego napisu to: {minDlugosc}\n")
