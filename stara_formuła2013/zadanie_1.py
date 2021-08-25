with open("dane_2013.txt", "r", encoding="UTF-8") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())

# print(liczby)

ile_liczb = 0

for liczba in liczby:
    if liczba[0] == liczba[len(liczba) - 1]:
        ile_liczb += 1

print(f'a) Liczb, w których pierwsza cyfra jest równa ostatniej jest: {ile_liczb}')

with open("wyniki6.txt", "w", encoding="UTF-8") as plik:
    plik.write(f'a) Liczb zapisanych w sustemie ósemkowym, w których pierwsza cyfra jest równa ostatniej jest: {ile_liczb}\n\n')
