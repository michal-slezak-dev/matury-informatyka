from string import ascii_uppercase
from collections import defaultdict

with open("instrukcje.txt", "r") as file:
    instructions = [line.split() for line in file]

"""
1. Tworzymy listę, która przechowuje duże litery alfaberu angielskiego.
2. Tworzymy słownik (defaultdict), który przechowuje w kluczach kolejne litery angielskiego alfabetu
a w wartościach literę następującą po literze z klucza.

Zaczynamy od i = 1, bo gdybyśmy zaczęli od 0 to przy ostatniej iteracji wywaliłoby nam błąd, że wyszliśmy poza zakres.
Na koniec dodajemy ten przypadek, że dla "Z" zamieniamy na "A" -> "Z": "A"
"""
letters = list(ascii_uppercase)
changed_letters = defaultdict(str)

for i in range(1, len(letters)):
    changed_letters[letters[i - 1]] = letters[i]

changed_letters.update({"Z": "A"})

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
                    string_list[string_list.index(letter)] = changed_letters[letter]
                    break

print("".join(string_list))
with open("wyniki4.txt", "a", encoding="UTF-8") as output:
    output.write("\n4.4\n")
    output.write("".join(string_list))