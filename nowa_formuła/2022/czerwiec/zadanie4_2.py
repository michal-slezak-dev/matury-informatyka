with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

# 1. method
nums_and_abs = {num: abs(int(num) - int(num[::-1])) for num in nums}  # slownik z kluczami - liczbami i wartosciami - abs z roznicy
max_diff = max(nums_and_abs.values())

for num in nums_and_abs:
    if nums_and_abs[num] == max_diff:
        max_num = num

# 2. method
max_diff = -1
max_num = 0

for num in nums:
    diff = abs(int(num) - int(num[::-1]))  # bardziej optymalna wersja, bo jedna petla
    if diff > max_diff:
        max_diff = diff
        max_num = num

with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("ZADANIE 4.2:\n")
    out.write(f"{max_num} {max_diff}\n")