with open("dane_2013.txt", "r", encoding="UTF-8") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())

# print(liczby)

liczby_dziesietne = []

for liczba in liczby:
    liczby_dziesietne.append(str(int(liczba, base=8)))

ile_liczb = 0

for liczba_dziesietna in liczby_dziesietne:
    if liczba_dziesietna[0] == liczba_dziesietna[len(liczba_dziesietna) - 1]:
        ile_liczb += 1

# print(liczby_dziesietne)

print(f'b) Tych liczb jest: {ile_liczb}')

with open("wyniki6.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'b) Liczb zapisanych w systemie dziesiętnym, w których pierwsza cyfra jest równa ostatniej jest: {ile_liczb}\n\n')
