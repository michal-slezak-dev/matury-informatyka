def najlepsza_suma(lista):
    najlepszaSuma = -1000000000000
    suma = 0

    for i in range(len(lista)):
        suma += int(lista[i])
        if suma > 0:
            if suma > najlepszaSuma:
                najlepszaSuma = suma
        else:
            suma = 0
    return najlepszaSuma

with open("dane5-1.txt", "r") as file:
    print(f' Naljepsza suma dla pliku dane5-1: {najlepsza_suma(list(file))}')

with open("dane5-2.txt", "r") as file:
    print(f' Naljepsza suma dla pliku dane5-2: {najlepsza_suma(list(file))}')

with open("dane5-3.txt", "r") as file:
    print(f' Naljepsza suma dla pliku dane5-3: {najlepsza_suma(list(file))}')
