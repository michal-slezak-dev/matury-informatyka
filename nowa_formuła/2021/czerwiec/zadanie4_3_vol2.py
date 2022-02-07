from string import ascii_uppercase, digits
from collections import deque
from copy import deepcopy

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

def transform_into_palindrome(string, chars):
    """
    Funkcja ta zwraca zmieniony w palindrom napis, jeśli się da
    :param string:
    :param chars:
    :return:
    """
    string = deque(string)

    for char in chars:

        deque_left = deepcopy(string)
        deque_right = deepcopy(string)

        deque_left.appendleft(char)
        deque_right.append(char)

        string_left = "".join(list(deque_left))
        string_right = "".join(list(deque_right))

        if is_palindrome(string_left):
            return string_left

        elif is_palindrome(string_right):
            return string_right

        elif not is_palindrome(string_left):
            deque_left.popleft()

        elif not is_palindrome(string_right):
            deque_right.pop()

with open("napisy.txt", "r") as file:
    strings = [line.strip() for line in file]

alphabet_and_digits = list(ascii_uppercase) + list(digits)

palindromes = []
for string in strings:
    transformed_string = transform_into_palindrome(string, alphabet_and_digits)

    if transformed_string is not None:
        palindromes.append(transformed_string)

password = ""
for palindrome in palindromes:
    password += palindrome[25]

print(password)
with open("wyniki4.txt", "a") as out:
    out.write("Zadanie 4.3\n")
    out.write(f"{password}\n\n")
