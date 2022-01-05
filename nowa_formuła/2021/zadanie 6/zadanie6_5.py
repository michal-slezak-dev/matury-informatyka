from collections import defaultdict
from pprint import pprint
with open("jednostki.txt", "r") as plik1:
    jednostki = []
    for linia in plik1:
        linia = linia.strip().split()
        if len(linia) == 5:
            jednostki.append((linia[0], linia[1], linia[2], linia[3], linia[4]))
        elif len(linia) == 6:
            nazwa_klasy = linia[2] + linia[3]
            jednostki.append((linia[0], linia[1], nazwa_klasy, linia[4], linia[5]))

jednostki.pop(0)

with open("gracze.txt", "r") as plik2:
    gracze = {linia.strip().split()[0] : linia.strip().split()[1] for linia in plik2}

del gracze["id_gracza"]

jednostki_pozycje = []
for jednostka in jednostki:
    jednostki_pozycje.append((jednostka[1], jednostka[3], jednostka[4]))

bitwy = defaultdict(int)
gracze_pozycje = defaultdict(list)
for tuple in jednostki_pozycje:
    bitwy[tuple[1:]] += 1
    gracze_pozycje[tuple[0]].append(tuple[1:])

liczniki = []
polskie_bitwy = 0
for tuple in bitwy:
    if bitwy[tuple] > 1:
        liczniki.append(1)
        for id in gracze_pozycje:
            if tuple in gracze_pozycje[id]:
                if gracze[id] == "Polska":
                    polskie_bitwy += 1

print(sum(liczniki))
print(polskie_bitwy)