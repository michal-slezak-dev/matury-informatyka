with open("napisy.txt", "r") as file:
    strings = [line.strip() for line in file]

num_of_digits = 0
for string in strings:
    for char in string:
        if char.isdigit():
            num_of_digits += 1

print(num_of_digits)
with open("wyniki4.txt", "w") as out:
    out.write("Zadanie 4.1\n")
    out.write(f"{num_of_digits}\n\n")