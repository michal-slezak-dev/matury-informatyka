def czy_p(napis):
    if napis == napis[::-1]:
        return True
    return False

with open("identyfikator.txt", "r") as plik:
    identyfikatory = [linia.strip() for linia in plik]

odp = []
for id in identyfikatory:
    """Oddzielam serię i cyfry"""
    seria = ""
    cyfry = []
    for znak in id:
        if not znak.isdigit(): # sprawdzam czy znak jest nie jest cyfrą jeśli nie - to seria
            seria += znak
        else: # jeśli tak to cyfra
            cyfry.append(znak)

    if czy_p(seria) or czy_p(cyfry): # sprawdzenie czy albo seria, albo część numeryczna jest palindromem, jesli tak - wypisujemy id
        print(id)
        odp.append(id)


with open("wyniki4_2.txt", "w", encoding='UTF-8') as out:
    out.write("Zadanie 4.2:\n")
    for id in odp:
        out.write(f"{id}\n")