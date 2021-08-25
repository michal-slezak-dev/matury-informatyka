with open("binarne.txt", "r", encoding="UTF-8") as file:
    napisy_binarne = []

    for line in file:
        napisy_binarne.append(line.strip())

# print(napisy_binarne)

# liczby dziesiętne mniejsze od 65 535
liczby_dziesietne = []

for napis in napisy_binarne:
    if int(napis, 2) < 65535:
        liczby_dziesietne.append(int(napis, 2))

# print(liczby_dziesietne)

najwieksza_dziesietna = max(liczby_dziesietne)
najwieksza_binarna = bin(najwieksza_dziesietna).lstrip("0b")

print(
    f"Największa liczba w systemie dziesiętnym: {najwieksza_dziesietna}\nZapis binarny tej liczby: {najwieksza_binarna}"
)

with open("zadanie4.txt", "a", encoding="UTF-8") as file:
    file.write(
        f"c) Największa liczba w systemie dziesiętnym: {najwieksza_dziesietna}\nZapis binarny tej liczby: {najwieksza_binarna}"
    )
