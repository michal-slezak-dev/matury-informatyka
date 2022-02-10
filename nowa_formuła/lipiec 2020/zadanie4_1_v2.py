def sum_of_the_numeric_part(id):
    """
    Funkcja, która zwraca nam sumę cyfr z części numerycznej identyfikatora
    :param id:
    :return:
    """
    return sum(list(map(int, id[3:])))

with open("identyfikator.txt", "r") as file:
    ids = []
    for line in file:
        ids.append(line.strip())

# lista, która przechowuje nam sumy części numerycznej dla danego id
sums_of_the_numeric_parts = []
for id in ids:
    sums_of_the_numeric_parts.append(sum_of_the_numeric_part(id))

max_sum = max(sums_of_the_numeric_parts) # wyłaniamy największą sumę

# wyłaniamy id, które mają największą sumę
max_ids = []
for id in ids:
    if sum_of_the_numeric_part(id) == max_sum:
        max_ids.append(id)

for max_id in max_ids:
    print(f"{max_id}")

with open("wyniki4_1.txt", "w", encoding="UTF-8") as output:
    for max_id in max_ids:
        output.write(f"{max_id}\n")