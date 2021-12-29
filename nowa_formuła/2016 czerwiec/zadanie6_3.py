with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

counter = 0
for num in nums:
    if num[-1] == "2":
        num = list(num)[:len(num) - 1]
        if int(''.join(num), 2) % 2 == 0:
            counter += 1

print(counter)