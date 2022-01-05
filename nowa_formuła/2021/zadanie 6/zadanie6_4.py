from collections import defaultdict
from pprint import pprint
with open("jednostki.txt", "r") as plik1:
    jednostki = []
    for linia in plik1:
        linia = linia.strip().split()
        if len(linia) == 5: # dodajemy do listy krotkę z informacjami o id_jednostki, id_gracza, nazwa, lok_x, lok_y
            jednostki.append((linia[0], linia[1], linia[2], linia[3], linia[4]))
        elif len(linia) == 6: # jeśli mamy nazwę klasy typu mag wody etc., tzn. złożoną z 2 członów to łączymy je i dodajemy do krotki razem z innymi informacjami
            nazwa_klasy = linia[2] + linia[3]
            jednostki.append((linia[0], linia[1], nazwa_klasy, linia[4], linia[5]))

jednostki.pop(0) # usuwamy krotkę, która ma nagłówki

with open("klasy.txt", "r") as plik2:
    klasy = {} # dla każdej z klas do słownika dodajemy nazwę klasy i jej szybkość
    for linia in plik2:
        linia = linia.strip().split()
        if len(linia) == 5: # jeśli nazwa ma jeden człon to dodajemy do kluczy nazwę klasy i do wartości jej szybkość
            klasy.update({linia[0] : linia[4]})
        elif len(linia) == 6: # jeśli nazwa klasy składa się z 2 członów, tak jak w przypadku jednostek, to łączymy te człony o dopiero potem do kluczy dodajemy złączoną nazwę i szybkość do wartości
            nazwa_klasy = linia[0] + linia[1]
            klasy.update({nazwa_klasy : linia[5]})

del klasy["nazwa"] # usuwamy nagłówki

BRAMA_X = 100 # pozycja_x bramy
BRAMA_Y = 100 # pozycja_y bramy

klasy_ilos_jedna_tura = defaultdict(int) # ten słownik będzie nam przechowywać w kluczach nazwę klasy, a w wartościach ilość jednostek tej klasy, która może w czasie jednej tury dojść do bramy
for jednostka in jednostki:
    if abs(int(jednostka[3]) - BRAMA_X) + abs(int(jednostka[4]) - BRAMA_Y)  <= int(klasy[jednostka[2]]): # warunek z polecenia
        klasy_ilos_jedna_tura[jednostka[2]] += 1 # do naszego defaultdict za każdym razem jeśli spełniony jest warunek zadania to dodajemy + 1 do danej klasy
pprint(klasy_ilos_jedna_tura) # wypisujemy wynik
