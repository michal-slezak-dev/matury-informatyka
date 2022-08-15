def is_prime(num):
    if num < 2:
        return False
    for i in range(3, num):
        if num % i == 0:
            return False
    return True

with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("ZADANIE 4.3:\n")

    for num in nums:
        if is_prime(int(num)) and is_prime(int(num[::-1])):  # sprawdzamy czy i liczba, i odbicie to liczby pierwsze
            out.write(f"{num} \n")