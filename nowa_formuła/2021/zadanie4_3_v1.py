# ta funkcja zwraca liczbę wystąpień danej litery w liście
def num_of_occurances_letter(list, letter):
    counter = 0
    for element in list:
        if element == letter:
            counter += 1

    return counter

# ta funkcja zwraca słownik, który w kluczach malitery, a w wartościach liczbę ich wystąpień w liście
def num_of_occuraces(list):
    occurances = dict()

    for letter in list:
        occurances.update({letter: num_of_occurances_letter(list, letter)})

    return occurances

# ta funkcja zwraca nam największy element w tablicy
def get_max(array):
    max_element = array[0]

    for element in array:
        if element > max_element:
            max_element = element

    return max_element

# ta funkcja zwraca nam listę wartości słownika
def get_dict_values(dict):
    values = []
    for key in dict:
        values.append(dict[key])

    return values

# ta funkcja zwraca literę, która jest dopisywana najczęściej i liczbę jej wystąpień
def get_dominant_letter(dict):
    max_num_of_occurances = get_max(get_dict_values(dict))

    for letter in dict:
        if dict[letter] == max_num_of_occurances:
            return letter, max_num_of_occurances

with open("instrukcje.txt", "r") as file:
    instructions = []
    for line in file:
        if line.strip().split()[0] == "DOPISZ":
            instructions.append(line.strip().split()[1])

# wywołujemy wszyskie potrzebne funkcje, aby otrzymać literę (dominantę) i ilość jej wystąpień
dominant_letter = get_dominant_letter(num_of_occuraces(instructions))
print(f"{dominant_letter[0]} {dominant_letter[1]}")

with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("\n4.2\n")
    out.write(f"{dominant_letter[0]} {dominant_letter[1]}\n\n")