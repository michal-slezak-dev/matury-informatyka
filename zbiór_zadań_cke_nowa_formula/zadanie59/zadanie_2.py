# Funkcja sprawdzająca czy dana liczba jest palindrommiczna
def czy_palindrom(liczba):
    if str(liczba) == str(liczba)[::-1]:
        return True
    return False

# Funkcja zwracająca odwróconą liczbę
def odwrocona(liczba):
    return int(str(liczba)[::-1])

with open("liczby (2).txt", "r") as plik:
    liczby = []

    for line in plik:
        liczby.append(int(line.strip()))
# print(liczby)

ile_liczb = 0

# Sprawdzamy czy suma tej liczby i liczby odwróconej jest liczbą palindromiczną, jesli tak to zwiększamy licznik
for liczba in liczby:
    if czy_palindrom(liczba + odwrocona(liczba)):
        ile_liczb += 1

print(f'Ilość liczb, których suma tej liczby i jej liczby odwróconej jest liczbą palindromiczną jest: {ile_liczb}')

with open("wyniki_liczby.txt", "a", encoding="UTF-8") as plik:
    plik.write("Zadanie 59.2\n")
    plik.write(f'Ilość liczb, których suma tej liczby i jej liczby odwróconej jest liczbą palindromiczną jest: {ile_liczb}\n\n')
