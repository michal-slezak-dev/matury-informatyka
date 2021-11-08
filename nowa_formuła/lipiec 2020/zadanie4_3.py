with open("identyfikator.txt", "r") as plik:
    identyfikatory = [linia.strip() for linia in plik]



zamiana = {}
znak = "A"
zamiana.update({znak: 10})
for i in range(11, 36):
    znak = chr(ord(znak) + 1)
    zamiana.update({znak: i})

odp = []
for id in identyfikatory:
    """Oddzielam serię i cyfry"""
    suma = 0
    seria = []
    cyfry = []
    seria_po_zamianie = [] # zamiana literek na liczby zgodnie z poleceniem

    for znak in id:
        if not znak.isdigit(): # sprawdzam czy znak jest nie jest cyfrą jeśli nie - to seria
            seria.append(znak)
        else: # jeśli tak to cyfra
            cyfry.append(int(znak))

    pierwsza = cyfry[0] # id[3] # wyznaczamy pierwszą cyfrę id(kontrolną)

    cyfry.pop(0) # usuwamy pierwszą cyfrę id(kontrolną)
    for zk in seria:
        seria_po_zamianie.append(zamiana[zk])

    razem = seria_po_zamianie + cyfry

    # suma cyfr z wyjątkiem kontrolnej(możńa w sumie funkcję też napisać sprawdzającą czy jest poprawny ;-) )
    suma = razem[0] * 7 + razem[1] * 3 + razem[2] * 1 + razem[3] * 7 + razem[4] * 3 + razem[5] * 1 + razem[6] * 7 + razem[7] * 3

    if suma % 10 != pierwsza: # sprawdzamy czy nie spełnia warunku - jeśli niespełnia - wypisujemy
        print(id)
        odp.append(id)


with open("wyniki4_3.txt", "w", encoding='UTF-8') as out:
    out.write("Zadanie 4.3:\n")
    for id in odp:
        out.write(f"{id}\n")

    
