from collections import defaultdict

with open("zadanie5_5_pom.txt", "r") as plik:
    # dodajemy do listy listę, która zawiera id_pokoju oraz tytuł wypożyczonej książki
    pokoje_tytuly = [[linia.strip().split()[0], linia.strip().split()[1:]] for linia in plik]

pokoje_tytuly.pop(0) # usuwamy nagłówki

with open("meldunek.txt", "r") as plik:
    # wczytujemy do listy listę zawierającą pesel i id_pok
    meldunki = [linia.strip().split() for linia in plik]

meldunki.pop(0) # usuwamy nagłówki

with open("wypozyczenia.txt", "r") as plik:
    # wczytujemy do listy listę zawierającą lp, pesel i tytul
    wypozyczenia = [linia.strip().split() for linia in plik]

wypozyczenia.pop(0) # usuwamy nagłówki

# Tutaj zajmujemy się osobami spoza miasteczka akademickiego
"""
Do listy [studenci_z_miasteczka] dodajemy pesele studentów, którzy mieszkają w miasteczku akademickim. Następnie, do listy [studenci_spoza_miasteczka] zapisujemy pesele studentów z listy wypozyczenia, którzy wypożyczyli książki,
ale nie są z miasteczka. Aby policzyć, ile osób spoza miasteczka wypożyczyło książki --> należy po prostu podać długość listy [studenci_spoza_miasteczka].
"""
studenci_z_miasteczka = [meldunek[0] for meldunek in meldunki]
studenci_spoza_miasteczka = [wypozyczenie[1] for wypozyczenie in wypozyczenia if wypozyczenie[1] not in studenci_z_miasteczka]

ilosc_studentow_spoza = len(studenci_spoza_miasteczka)  # długość listy z numerami pesel studentów, którzy wypożyczyli książki i są spoza miasteczka

# tutaj zajmujemy się osobami, które mieszkają w miasteczku akademickim
# zamieniamy listę z fragmentami tytułu książki na napis (string)
for pokoj_tytul in pokoje_tytuly:
    nowy = ""
    for element in pokoj_tytul[1]:
        nowy += element + " "
    pokoj_tytul[1] = nowy

"""
Słownik ten będzie w kluczach przechowywać id_pokoju a w wartościach zbiór z unikalnymi tytułami wypożyczonych książek, 
dzięki czemu wyłączamy z tego wypożyczenia tych samych książek przez osoby z tego samgo pokoju. Robimy tak, aby żadna książka nie powtórzyła się
w tym samym pokoju. Warto zauważyć, że do tego uzywam defaultdicta
"""
unikalne_w_pokoju = defaultdict(set)
for pokoj in pokoje_tytuly:
    unikalne_w_pokoju[pokoj[0]].add(pokoj[1])


# Ten słownik przechowuje w kluczach id_pokoju a w wartościach ilość (długość zbioru) różnych (unikalnych) książek w danym pokoju.
pokoj_liczba = defaultdict(int)
for pokoj in unikalne_w_pokoju:
    pokoj_liczba[pokoj] = len(unikalne_w_pokoju[pokoj])

# Wynikiem jest suma długości zbiorów ze słownika {pokoj_liczba} powiększona o ilosc wypozyczonych książek przez studentów spoza kampusu
print(sum(pokoj_liczba.values()) + ilosc_studentow_spoza)