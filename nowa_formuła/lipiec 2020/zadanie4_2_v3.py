def is_a_palindrome(id):
    """
    Funkcja, która sprawdza nam czy albo seria, albo część numeryczna to palindrom
    :param id:
    :return:
    """
    series = id[:3]
    numeric_part = id[3:]

    return series == series[::-1] or numeric_part == numeric_part[::-1]

with open("identyfikator.txt", "r") as file:
    ids = [line.strip() for line in file]

# zapisujemy te id, w których albo seria, albo część numeryczna to palindrom
palindromes = [id for id in ids if is_a_palindrome(id)]
for palindrome in palindromes:
    print(f"{palindrome}")

with open("wyniki4_2.txt", "w", encoding="UTF-8") as output:
    for palindrome in palindromes:
        output.write(f"{palindrome}\n")