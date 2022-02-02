from collections import Counter

with open("instrukcje.txt", "r") as file:
    instructions = [line.strip().split()[0] for line in file]

# Wystarczy, że policzymy ile jest instrukcji DOPISZ i odejmiemy od tego ilość instrukcji USUN
length = Counter(instructions)["DOPISZ"] - Counter(instructions)["USUN"]

print(length)

with open("wyniki4.txt", "w", encoding='UTF-8') as out:
    out.write("4.1\n")
    out.write(str(length) + "\n")
