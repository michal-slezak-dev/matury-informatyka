def division(num_list):
    div_2 = 0
    div_3 = 0
    div_5 = 0

    for number in num_list:
        if number % 2 == 0:
            div_2 += 1
        if number % 3 == 0:
            div_3 += 1
        if number % 5 == 0:
            div_5 += 1

    # msg_div = str(div_2) + " " + str(div_3) + " " + str(div_5)

    return div_2, div_3, div_5


# PLIK LICZBY1.TXT
with open("liczby1.txt", "r") as file:
    decimal_nums_1 = []

    for line in file:
        decimal_nums_1.append(int(line.strip(), 2))
# print(decimal_nums_1)

# PLIK LICZBY2.TXT
with open("liczby2.txt", "r") as file2:
    decimal_nums_2 = []

    for line in file2:
        decimal_nums_2.append(int(line.strip(), 2))
# print(decimal_nums_2)

# PLIK LICZBY3.TXT
with open("liczby3.txt", "r") as file3:
    decimal_nums_3 = []

    for line in file3:
        decimal_nums_3.append(int(line.strip(), 2))
# print(decimal_nums_3)

#plik liczby1.txt
print(f' Liczb podzielnych przez 2 w pliku liczby1.txt jest: {division(decimal_nums_1)[0]}')
print(f' Liczb podzielnych przez 3 w pliku liczby1.txt jest: {division(decimal_nums_1)[1]}')
print(f' Liczb podzielnych przez 5 w pliku liczby1.txt jest: {division(decimal_nums_1)[2]}\n')

print(f' Liczb podzielnych przez 2 w pliku liczby2.txt jest: {division(decimal_nums_2)[0]}')
print(f' Liczb podzielnych przez 3 w pliku liczby2.txt jest: {division(decimal_nums_2)[1]}')
print(f' Liczb podzielnych przez 5 w pliku liczby2.txt jest: {division(decimal_nums_2)[2]}\n')

print(f' Liczb podzielnych przez 2 w pliku liczby3.txt jest: {division(decimal_nums_3)[0]}')
print(f' Liczb podzielnych przez 3 w pliku liczby3.txt jest: {division(decimal_nums_3)[1]}')
print(f' Liczb podzielnych przez 5 w pliku liczby3.txt jest: {division(decimal_nums_3)[2]}\n')

with open("podzielnosc.txt", "w") as outputFile:
    outputFile.write(f' Liczb podzielnych przez 2 w pliku liczby1.txt jest: {division(decimal_nums_1)[0]}\n')
    outputFile.write(f' Liczb podzielnych przez 3 w pliku liczby1.txt jest: {division(decimal_nums_1)[1]}\n')
    outputFile.write(f' Liczb podzielnych przez 5 w pliku liczby1.txt jest: {division(decimal_nums_1)[2]}\n\n')

    outputFile.write(f' Liczb podzielnych przez 2 w pliku liczby2.txt jest: {division(decimal_nums_2)[0]}\n')
    outputFile.write(f' Liczb podzielnych przez 3 w pliku liczby2.txt jest: {division(decimal_nums_2)[1]}\n')
    outputFile.write(f' Liczb podzielnych przez 5 w pliku liczby2.txt jest: {division(decimal_nums_2)[2]}\n\n')

    outputFile.write(f' Liczb podzielnych przez 2 w pliku liczby3.txt jest: {division(decimal_nums_3)[0]}\n')
    outputFile.write(f' Liczb podzielnych przez 3 w pliku liczby3.txt jest: {division(decimal_nums_3)[1]}\n')
    outputFile.write(f' Liczb podzielnych przez 5 w pliku liczby3.txt jest: {division(decimal_nums_3)[2]}\n\n')
