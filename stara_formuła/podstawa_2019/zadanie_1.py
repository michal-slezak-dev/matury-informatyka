def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


with open("dane_2019.txt", "r") as plik:
    lista_danych = []
    for line in plik:
        lista_danych.append(line.replace("\n", ""))

# print(lista_danych)

kobiety = 0
mezczyzni = 0

for pesel in lista_danych:
    # print(pesel)
    if czy_parzysta(int(pesel[9])):
        kobiety += 1
    else:
        mezczyzni += 1


print(kobiety, " ", mezczyzni)

with open("odpowiedziPESEL.txt", "w", encoding="UTF-8") as plik:
    plik.write("a)\n Liczba kobiet: ")
    plik.write(str(kobiety))
    plik.write("\nLiczba mężczyzn: ")
    plik.write(str(mezczyzni))
