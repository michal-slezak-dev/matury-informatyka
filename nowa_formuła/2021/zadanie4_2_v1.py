def get_max(array):
    max_element = array[0]

    for element in array:
        if element > max_element:
            max_element = element

    return max_element

with open("instrukcje.txt", "r") as file:
    instructions = []
    for line in file:
        instructions.append(line.strip().split()[0])

"""
Tworzymy listę [instructions_and_num], która przechowuje nam tuple z instrukcją i ilością występujących po sobie
takich samych instrukcji. Tworzymy też zmienną counter, która będzie nam po prostu zliczała ilość tych samych
instrukcji występujących po sobie.
Jeśli kolejna istrukcja jest taka sama to zwiększamy counter o 1, jeśli nie to przypisujemy mu wartość 1, następnie 
dodajemy krotkę z instrukcją i ilością tych samych instrukcji występujących po sobie do listy [instructions_and_num]
"""
instructions_and_num = []
counter = 1
for i in range(1, len(instructions)):
    if instructions[i] == instructions[i - 1]:
        counter += 1
    else:
        counter = 1

    instructions_and_num.append((instructions[i], counter))

# ta lista przechowuje tylko liczbę wystąpień tych samych instrukcji po sobie
only_num_of_occurances = []
for instruction in instructions_and_num:
    only_num_of_occurances.append(instruction[1])

# wyłaniamy największą liczbę takich samych instrukcji występujących po sobie
max_num = get_max(only_num_of_occurances)

# wyłaniamy instrukcję, która występowała najwięcej razy po sobie
for instruction in instructions_and_num:
    if instruction[1] == max_num:
        max_instruction = instruction[0]

print(f"{max_instruction} {max_num}")

with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("\n4.2\n")
    out.write(f"{max_instruction} {max_num}\n\n")