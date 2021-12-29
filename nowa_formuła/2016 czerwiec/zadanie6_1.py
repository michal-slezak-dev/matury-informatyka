with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

octal = 0
for num in nums:
    if num[-1] == "8": octal += 1

print(octal)