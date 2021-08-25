from pprint import pprint
with open("slowa (4).txt", "r", encoding="UTF-8") as plik:
    slowa_binarne = []

    for line in plik:
        slowa_binarne.append(line.strip())

# print(slowa_binarne)

najdluzsze_ciagi_w_slowie = {}

for slowo in slowa_binarne:
    ciag_zer = 0
    najdluzszy_ciag_aktualny = 0
    for i in range(1, len(slowo) + 1):
        if slowo[i - 1] != '0':
            ciag_zer = 0
        else:
            ciag_zer += 1
            if ciag_zer > najdluzszy_ciag_aktualny:
                    najdluzszy_ciag_aktualny = ciag_zer
                    najdluzsze_ciagi_w_slowie.update({slowo: najdluzszy_ciag_aktualny})

# print(najdluzsze_ciagi_w_slowie)

max_ciag = max(najdluzsze_ciagi_w_slowie.values())

print(f'c) Nadjłuższy ciąg ma długość: {max_ciag}')
print(f'Słowa zawierające ten ciąg to: ')

slowa_z_max_ciagiem = []
for klucz in najdluzsze_ciagi_w_slowie:
    if najdluzsze_ciagi_w_slowie[klucz] == max_ciag:
        print(klucz)
        slowa_z_max_ciagiem.append(klucz)


with open("wyniki4.txt", "a", encoding='UTF-8') as plik2:
    plik2.write(f' \n c) Nadjłuższy ciąg ma długość: {max_ciag} \n')
    plik2.write(f'Te słowa to: \n')
    for slowo in slowa_z_max_ciagiem:
        plik2.write(str(slowo) + "\n")
