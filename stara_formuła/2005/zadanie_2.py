def najlepsza_suma(lista, dlugosc):
    najlepszaSuma = -1000000000000
    suma = 0

    for i in range(dlugosc):
        suma += lista[i]

        if suma > 0:
            if suma > najlepszaSuma:
                najlepszaSuma = suma
        else:
            suma = 0
    return najlepszaSuma


with open("dane5-1.txt", "r", encoding="UTF-8") as plik:
    liczby_1 = []
    for line in plik:
        liczby_1.append(int(line.strip()))
# print(liczby_1)

print(f' Naljepsza suma dla pliku dane5-1: {najlepsza_suma(liczby_1, len(liczby_1))}')

with open("dane5-2.txt", "r", encoding="UTF-8") as plik:
    liczby_2 = []
    for line in plik:
        liczby_2.append(int(line.strip()))
# print(liczby_2)

print(f' Naljepsza suma dla pliku dane5-2: {najlepsza_suma(liczby_2, len(liczby_2))}')

with open("dane5-3.txt", "r", encoding="UTF-8") as plik:
    liczby_3 = []
    for line in plik:
        liczby_3.append(int(line.strip()))
# print(liczby_3)

print(f' Naljepsza suma dla pliku dane5-3: {najlepsza_suma(liczby_3, len(liczby_3))}')
