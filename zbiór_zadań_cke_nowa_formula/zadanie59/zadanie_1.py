from math import sqrt

# Rozkładamy liczbę na czynniki pierwsze, jeśli liczba jest parzysta t trzeba ją odrzucić, ponieważ potrzebujemy dzielników, które są
# liczbami pierwszymi i są nieparzyste, dlatego też w pętli zaczynamy od 3 i krok co 2, zeby miec nieparzyste
# jeżeli liczba % dzielnik daje reszte 0 to wtedy dzielimy taka liczbe całkowicie przez ten dzielnik i do listy czynniki dodajemy dziel, bo jest to nasz czynniok pierwszy
# na koniec sprawdzamy resztki liczby, jeśli nie zostały znalezione w pętli to są też czynnikami
def rozklad(num):
    czynniki = []

    if num % 2 == 0:
        return czynniki
    for dziel in range(3, int(sqrt(num)), 2):
        while num % dziel == 0:
            num //= dziel
            czynniki.append(dziel)
    if num != 1:
        czynniki.append(num)
    return czynniki


with open("liczby (2).txt", "r") as plik:
    liczby = []

    for line in plik:
        liczby.append(int(line.strip()))
# print(liczby)
#test
# print(rozklad(1331))

ile_liczb = 0

# Pętla, w której tworzymy set, który będzie posiadał unikalne elementy
# elementy w secie są unikalne, nie powtarzają się, więc będziemy tam zapisywać różne czynniki
# jeżeli czynników jest równo 3 to zwiększamy licznik i na końcu wyświetlamy wynik
for liczba in liczby:
    czy_rozne = set()
    for czynnik in rozklad(liczba):
        czy_rozne.add(czynnik)
    if len(czy_rozne) == 3:
        ile_liczb += 1

print(f'Liczb, w których rozkładzie występują dokładnie 3 różne czynniki pierwsze jest: {ile_liczb}')

with open("wyniki_liczby.txt", "w", encoding="UTF-8") as plik:
    plik.write("Zadanie 59.1\n")
    plik.write(f'Liczb, w których rozkładzie występują dokładnie 3 różne czynniki pierwsze jest: {ile_liczb}\n\n')
