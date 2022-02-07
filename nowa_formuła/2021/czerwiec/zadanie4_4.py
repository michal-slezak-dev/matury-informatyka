def only_digits(string):
    digits = [char for char in string if char.isdigit()]

    if len(digits) % 2 != 0:
        digits.pop()

    return digits

def group_given_digits(digits):
    grouped = []
    for i in range(1, len(digits), 2):
        grouped.append(int(digits[i - 1] + digits[i]))

    return grouped


with open("napisy.txt", "r") as file:
    strings = [line.strip() for line in file]

password = ""
x_counter = 0
for string in strings:
    for num in group_given_digits(only_digits(string)):
        if 65 <= num <= 90:
            password += str(chr(num))

    for i in range(2, len(password)):
        if password[i - 2] == password[i - 1] == password[i] == "X":
            x_counter = 3
        else:
            x_counter = 0

    if x_counter == 3:
        break

print(password)
with open("wyniki4.txt", "a") as out:
    out.write("Zadanie 4.4\n")
    out.write(f"{password}\n\n")
