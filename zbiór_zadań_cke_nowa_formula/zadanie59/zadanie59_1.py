def unique_prime_factors(num):
    factors = []
    if num % 2 == 0:  # parzyste nie, bo maja zawsze arzysty czynnik -> 2
        return factors
    for i in range(2, int(num ** 0.5)):
        while num % i == 0:
            num //= i
            if i % 2 != 0:
                factors.append(i)
    if num != 1:
        factors.append(num)
    return len(set(factors))


with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

counter = 0
for num in nums:
    if unique_prime_factors(num) == 3:
        counter += 1

print(counter)

with open("wyniki_liczby.txt", "w", encoding="UTF-8") as out:
    out.write("59.1\n")
    out.write(f"{counter}\n\n")