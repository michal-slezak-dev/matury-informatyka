def is_a_palindrome(id):
    """
    Funkcja, która sprawdza nam czy albo seria, albo część numeryczna to palindrom
    :param id:
    :return:
    """
    series = id[:3]
    numeric_part = id[3:]

    if series == series[::-1] or numeric_part == numeric_part[::-1]:
        return True
    return False

with open("identyfikator.txt", "r") as file:
    ids = []
    for line in file:
        ids.append(line.strip())

# zapisujemy te id, w których albo seria, albo część numeryczna to palindrom
palindromes = []
for id in ids:
    if is_a_palindrome(id):
        palindromes.append(id)

for palindrome in palindromes:
    print(f"{palindrome}")

with open("wyniki4_2.txt", "w", encoding="UTF-8") as output:
    for palindrome in palindromes:
        output.write(f"{palindrome}\n")