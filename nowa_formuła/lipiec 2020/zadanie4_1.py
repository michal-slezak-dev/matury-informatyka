with open("identyfikator.txt", "r") as plik:
    identyfikatory = [linia.strip() for linia in plik]

sumy = []
id_nowe = {}

for id in identyfikatory:
    """Oddzielam serię i cyfry"""
    seria = ""
    cyfry = []
    for znak in id:
        if not znak.isdigit(): # sprawdzam czy znak jest nie jest cyfrą jeśli nie - to seria
            seria += znak
        else: # jeśli tak to cyfra
            cyfry.append(int(znak))
        
    suma = sum(cyfry) # sumujemy cyfry
    sumy.append(suma)
    id_nowe.update({id: suma}) # dla każdego id dodajemy obok sume jego cyfr

max_suma = max(sumy) # wyznaczamy max

odp = []
for id in id_nowe:
    if id_nowe[id] == max_suma: # wypisujemy id o najwiekszej sumie
        print(id)
        odp.append(id)

with open("wyniki4_1.txt", "w", encoding='UTF-8') as out:
    out.write("Zadanie 4.1:\n")
    for id in odp:
        out.write(f"{id}\n")
