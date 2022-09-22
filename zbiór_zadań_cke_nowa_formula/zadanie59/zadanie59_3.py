def digits_product(num):
    prod = 1
    for digit in list(str(num)):
        prod *= int(digit)

    return prod

def power(num, initial_product):
    product = initial_product
    k = 1  # bo jeden iloczy juz mamy -> ten początkowy

    while len(str(product)) != 1:
        product = digits_product(product)
        k += 1

    return k


with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

powers = {num: power(num, digits_product(num)) for num in nums}
powers_nums = {i: list(powers.values()).count(i) for i in range(1, 9)}
print(powers_nums)

powers_1 = [num for num in powers if powers[num] == 1]
max_1 = max(powers_1)
min_1 = min(powers_1)
print(max_1)
print(min_1)

with open("wyniki_liczby.txt", "a", encoding="UTF-8") as out:
    out.write("59.3\n")
    out.write("Moce: ilość liczb\n")
    for power in powers_nums:
        out.write(f"{power}: {powers_nums[power]}\n")
    out.write(f"\nMaksymalna liczba o mocy 1: {max_1}\n")
    out.write(f"Minimalna liczba o mocy 1: {min_1}\n")
