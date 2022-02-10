def check_if_valid(id):
    """
    Funkcja, która sprawdza nam czy dane id jest poprawne
    :param id:
    :return:
    """
    # klucze -> litery alfabetu, wartości -> odpowiednie liczby zgodnie z poleceniem
    convert_letters_to_nums = {}
    for i in range(65, 91):
        convert_letters_to_nums.update({chr(i): i - 55})

    # wyłaniamy samą serię i zamieniamy litery na liczby
    series = []
    for i in range(3):
        series.append(convert_letters_to_nums[id[i]])

    check_digit = int(id[3]) # cyfra kontrolna
    numeric_part = list(map(int, id[4:]))  # wyłaniamy resztę cyfr z części numerycznej i zamieniamy na inty

    sum_of_multiplied_nums = series[0] * 7 + series[1] * 3 + series[2] + numeric_part[0] * 7 + numeric_part[1] * 3 + numeric_part[2] + numeric_part[3] * 7 + numeric_part[4] * 3

    if sum_of_multiplied_nums % 10 == check_digit:
        return True
    return False

with open("identyfikator.txt", "r") as file:
    ids = []
    for line in file:
        ids.append(line.strip())

# wyłaniamy niepoprawne id
invalid_ids = []
for id in ids:
    if not check_if_valid(id):
        invalid_ids.append(id)

for invalid_id in invalid_ids:
    print(f"{invalid_id}")

with open("wyniki4_3.txt", "w", encoding="UTF-8") as output:
    for invalid_id in invalid_ids:
        output.write(f"{invalid_id}\n")