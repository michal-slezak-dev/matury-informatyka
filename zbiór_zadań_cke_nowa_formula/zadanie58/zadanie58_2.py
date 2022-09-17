# S1 - binarny S2 - czwórkowy S3 - ósemkowy
def from_system_to_decimal(num, sys):
    num = list(map(int, list(num)))
    dec = []

    i = len(num) - 1
    k = 0
    while i >= 0:
        dec.append(num[i] * (sys ** k))
        k += 1
        i -= 1

    return sum(dec)

with open("dane_systemy1.txt", "r") as file1:
    with open("dane_systemy2.txt", "r") as file2:
        with open("dane_systemy3.txt", "r") as file3:
            s1 = [from_system_to_decimal(line.strip().split(" ")[0], 2) for line in file1]
            s2 = [from_system_to_decimal(line.strip().split(" ")[0], 4) for line in file2]
            s3 = [from_system_to_decimal(line.strip().split(" ")[0], 8) for line in file3]

i = 0
counter = 0
while i < len(s1):
    if (s1[i] - 12) % 24 != 0 and (s2[i] - 12) % 24 != 0 and (s3[i] - 12) % 24 != 0:
        counter += 1
    i += 1


print(counter)

with open("wyniki_systemy.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 58.2\n")
    out.write(f"Liczba pomiarów, w których stan pomiaru był jednocześnie niepoprawny we wszystkich stacjach: {counter}\n")


