from string import ascii_uppercase, digits
from collections import deque
from copy import deepcopy

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

def transform_into_palindrome(string, chars):
    string = deque(string) # to do: sprobowac zrobic tak, ze na jednym napisie operuje a nie na 2 kopiach

    for char in chars:

        string_left = deepcopy(string)
        string_right = deepcopy(string)

        string_left.appendleft(char)
        string_right.append(char)

        if is_palindrome("".join(list(string_left))):
            return "".join(list(string_left))
        elif is_palindrome("".join(list(string_right))):
            return "".join(list(string_right))
        elif not is_palindrome("".join(list(string_left))):
            string_left.popleft()
        elif not is_palindrome("".join(list(string_right))):
            string_right.pop()

with open("napisy.txt", "r") as file:
    strings = [line.strip() for line in file]

alphabet_and_digits = list(ascii_uppercase) + list(digits)

palindromes = []
for string in strings:
    palindromes.append(transform_into_palindrome(string, alphabet_and_digits))

palindromes = list(filter(lambda x: x is not None, palindromes))

password = ""
for palindrome in palindromes:
    password += palindrome[25]

print(password)
with open("wyniki4.txt", "a") as out:
    out.write("Zadanie 4.3\n")
    out.write(f"{password}\n\n")
