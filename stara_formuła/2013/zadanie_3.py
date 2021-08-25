with open("dane_2013.txt", "r", encoding="UTF-8") as plik:
    liczby = []
    for line in plik:
        liczby.append(line.strip())

# print(liczby)

ile_liczb = 0
liczby_spelniajace_warunek = []


for liczba in liczby:
    for i in range(1, len(liczba)):
        if liczba[i - 1] > liczba[i]:
            break
        if i == len(liczba) - 1:
            ile_liczb += 1
            liczby_spelniajace_warunek.append(int(liczba, 8))


print(f'c) Liczb spełniających warunek jest: {ile_liczb}')
print(f'Najwieksza ósemkowa liczba spełniająca warunek: {oct(max(liczby_spelniajace_warunek)).lstrip("0o")} , w sysytemie dziesiętnym: {max(liczby_spelniajace_warunek)}')
print(f'Najmniejsza ósemkowa liczba spełniająca warunek: {oct(min(liczby_spelniajace_warunek)).lstrip("0o")} , w sysytemie dziesiętnym: {min(liczby_spelniajace_warunek)}')

with open("wyniki6.txt", "a", encoding="UTF-8") as plik:
    plik.write(f'c) Liczb spełniających warunek jest: {ile_liczb}\n')
    plik.write(f'Najwieksza ósemkowa liczba spełniająca warunek: {oct(max(liczby_spelniajace_warunek)).lstrip("0o")} , w sysytemie dziesiętnym: {max(liczby_spelniajace_warunek)} \n')
    plik.write(f'Najmniejsza ósemkowa liczba spełniająca warunek: {oct(min(liczby_spelniajace_warunek)).lstrip("0o")} , w sysytemie dziesiętnym: {min(liczby_spelniajace_warunek)}')
