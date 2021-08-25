with open("NAPISY_2014.TXT", "r", encoding="UTF-8") as plik:
    napisy = []

    for line in plik:
        napisy.append(line.strip())

# print(napisy)

napisy_wystepujace_wiecej_niz_raz_duplikaty = []
napisy_wystepujace_wiecej_niz_raz= []

for napis in napisy:
    if napisy.count(napis) > 1:
        napisy_wystepujace_wiecej_niz_raz_duplikaty.append(napis)

"""#1 SPOSÓB, ALE NAPISY SĄ W INNEJ KOLEJNOŚCI JAKO LISTA"""
# napisy_wystepujace_wiecej_niz_raz = list(set(napisy_wystepujace_wiecej_niz_raz_duplikaty))
# for napis in napisy_wystepujace_wiecej_niz_raz:
#     print(napis)

"""#2 SPOSÓB"""
for napis in napisy_wystepujace_wiecej_niz_raz_duplikaty:
    if napis not in napisy_wystepujace_wiecej_niz_raz:
        napisy_wystepujace_wiecej_niz_raz.append(napis)

for napis in napisy_wystepujace_wiecej_niz_raz:
    print(napis)

with open("ZADANIE5.TXT", "a", encoding="UTF-8") as plik:
    plik.write("c) Napisy, które wystąpiły więcej niż 1 raz: \n")

    for napis in napisy_wystepujace_wiecej_niz_raz:
        plik.write(f'{napis}\n')
