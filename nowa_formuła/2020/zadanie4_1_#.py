def is_prime(num):
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

with open("pary.txt", "r") as file:
    nums = [int(line.strip().split()[0]) for line in file]

with open("wyniki4.txt", "w") as out:
    out.write("ZADANIE 4.1\n")
    for num in nums:
        if num % 2 == 0 and num > 4:
            for i in range(2, num):
                if is_prime(i) and is_prime(num - i):
                    print(f"{num} {i} {num - i}")
                    out.write(f"{num} {i} {num - i}\n")
                    break
