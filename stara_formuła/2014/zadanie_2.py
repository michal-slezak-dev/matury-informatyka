with open("NAPISY_2014.TXT", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

# print(napisy)

napisy_rosnace = []
#ABCD -> 4 -> ROSNĄCY
#BCDA  -> 4 -> NIEROSNĄCY
for napis in napisy:
    for i in range(1, len(napis)):
        if ord(napis[i]) <= ord(napis[i - 1]):
            # napisy_rosnace.append(napis)
            break
        if i == len(napis) - 1:
            napisy_rosnace.append(napis)

# print(napisy_rosnace)

for napis in napisy_rosnace:
    print(napis)

with open("ZADANIE5.TXT", "a", encoding="UTF-8") as plik:
    plik.write(f'b) Napisy rosnące: \n')
    for napis in napisy_rosnace:
        plik.write(f'{napis}\n')
    plik.write("\n")
