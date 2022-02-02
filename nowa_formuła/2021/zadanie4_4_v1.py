# ta funkcja zwraca nam indeks pierwszego wystąpienia danej listery
def first_occurance(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

with open("instrukcje.txt", "r") as file:
    instructions = []

    for line in file:
        instructions.append(line.split())

"""
Tworzymy słownik, który w kluczach przechowuje kolejne litery alfabetu angielskiego,
a w wartościach następne literyw tym alfabecie, np. "A" : "B".

Kody ASCII wielkich liter alfabetu angielskiego są w przedziale 65 - 92,
dlatego też zaczynamy od 66 i kończymy na o 1 większym od 92, czyli 93, bo może wywalić nam
błąd, że poza zakres wyszliśmy. Jeśli i ma wartość Z, to zgodnie z poleceniem wartością do tego
klucza będzie A, jeśli nie to dodajemy po prostu do kluczy wartość i - 1(bo zaczynaliśmy o 1 więcej)
, a do wartości i. Oczywiście zamieniając i najpierw na char a potem na string.
"""
changed_letters = dict()
for i in range(66, 65 + 27):
    if i == 65 + 26:
        changed_letters.update({"Z": "A"})
    else:
        changed_letters.update({str(chr(i - 1)): str(chr(i))})

# tutaj wykonujemy operacje, zgodne z poleceniem, na liście, która przechowuje literki napisu
string_list = []
for instruction in instructions:
    if instruction[0] == "DOPISZ":
        string_list.append(instruction[1])
    elif instruction[0] == "ZMIEN":
        string_list[-1] = instruction[1]
    elif instruction[0] == "USUN":
        string_list.pop(-1)
    elif instruction[0] == "PRZESUN":
        if instruction[1] in string_list:
            for letter in string_list:
                if letter == instruction[1]:
                    string_list[first_occurance(string_list, letter)] = changed_letters[letter]
                    break

# dodajemy do zmiennej text poszczególne literki z listy
text = ""
for letter in string_list:
    text += letter

print(text)
with open("wyniki4.txt", "a", encoding="UTF-8") as output:
    output.write("\n4.4\n")
    output.write(text)