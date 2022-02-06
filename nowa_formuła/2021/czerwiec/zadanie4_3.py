from string import ascii_uppercase, digits
from collections import deque
from copy import deepcopy

def czy_palindrom(napis):
    if napis == napis[::-1]:
        return True
    return False

def zamiana_na_palindrom(napis, znaki):
    napis = deque(napis) # to do: sprobowac zrobic tak, ze na jednym napisie operuje a nie na 2 kopiach

    for znak in znaki:
        napis_lewo = deepcopy(napis)
        napis_prawo = deepcopy(napis)

        napis_lewo.appendleft(znak)
        napis_prawo.append(znak)

        if czy_palindrom("".join(list(napis_lewo))):
            return "".join(list(napis_lewo))
        elif czy_palindrom("".join(list(napis_prawo))):
            return "".join(list(napis_prawo))
        elif not czy_palindrom("".join(list(napis_lewo))):
            napis_lewo.popleft()
        elif not czy_palindrom("".join(list(napis_prawo))):
            napis_prawo.pop()

with open("napisy.txt", "r") as plik:
    napisy = [linia.strip() for linia in plik]

alfabet_i_cyfry = list(ascii_uppercase) + list(digits)

palindromy = []
for napis in napisy:
    palindromy.append(zamiana_na_palindrom(napis, alfabet_i_cyfry))

palindromy = list(filter(lambda x: x != None, palindromy))

haslo = ""
for palindrom in palindromy:
    haslo += palindrom[25]

print(haslo)
# with open("wyniki4.txt", "a") as out:
#     out.write("Zadanie 4.3\n")
#     out.write(f"{haslo}\n\n")
