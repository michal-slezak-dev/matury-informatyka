with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

four = 0
for num in nums:
    if num[-1] =="4" and "0" not in num: four += 1

print(four)