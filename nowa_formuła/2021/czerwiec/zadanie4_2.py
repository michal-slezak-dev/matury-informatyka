with open("napisy.txt", "r") as file:
    strings = [line.strip() for line in file]

position = 0
password = ""
for i in range(19, len(strings), 20):
    password += strings[i][position]
    position += 1

print(password)
with open("wyniki4.txt", "a") as out:
    out.write("Zadanie 4.2\n")
    out.write(f"{password}\n\n")
