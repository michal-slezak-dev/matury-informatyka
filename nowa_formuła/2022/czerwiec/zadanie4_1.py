with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

with open("wyniki4.txt", "w", encoding="UTF-8") as out:
    out.write("ZADANIE 4.1\n")
    for num in nums:
        if int(str(num)[::-1]) % 17 == 0:  # sprawdzam czy odbicie jest podzielne przez 17
            out.write(f"{num[::-1]}\n")