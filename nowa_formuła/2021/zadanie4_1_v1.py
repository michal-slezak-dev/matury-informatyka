with open("instrukcje.txt", "r") as file:
    instructions = []
    for line in file:
        instructions.append(line.strip().split()[0])


# Wystarczy, że policzymy ile jest instrukcji DOPISZ i odejmiemy od tego ilość instrukcji USUN
counter = 0
for instruction in instructions:
    if instruction == "DOPISZ": counter += 1
    elif instruction == "USUN": counter -= 1

print(counter)

with open("wyniki4.txt", "w", encoding='UTF-8') as out:
    out.write("4.1\n")
    out.write(str(counter) + "\n")