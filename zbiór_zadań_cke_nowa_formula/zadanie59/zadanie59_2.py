def is_palindromic(num):
    return str(num) == str(num)[::-1]


with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

counter = 0
for num in nums:
    if is_palindromic(num + int(str(num)[::-1])):
        counter += 1

print(counter)

with open("wyniki_liczby.txt", "a", encoding="UTF-8") as out:
    out.write("59.2\n")
    out.write(f"{counter}\n\n")