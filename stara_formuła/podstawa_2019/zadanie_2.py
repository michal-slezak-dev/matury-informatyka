with open("dane_2019.txt", "r") as plik:
    lista_danych = []
    for line in plik:
        lista_danych.append(line.replace("\n", ""))


listopad = 0

for pesel in lista_danych:
    if pesel[2] == "1" and pesel[3] == "1" or pesel[2] == "3" and pesel[3] == "1":
        listopad += 1

print(listopad)


with open("odpowiedziPESEL.txt", "a", encoding="UTF-8") as plik:
    plik.write("b)\n Liczba osób urodzonych w listopadzie: ")
    plik.write(str(listopad))
