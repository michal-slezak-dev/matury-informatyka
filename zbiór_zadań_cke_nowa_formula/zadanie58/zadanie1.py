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

def is_negative(num, system):
    num = list(num)

    if '-' in num:
        return int(f"-{from_system_to_decimal(''.join(num[1:]), system)}")
    else:
        return from_system_to_decimal(''.join(num), system)


with open("dane_systemy1.txt", "r") as file1:
    with open("dane_systemy2.txt", "r") as file2:
        with open("dane_systemy3.txt", "r") as file3:
            s1 = [is_negative(line.strip().split(" ")[1], 2) for line in file1]
            s2 = [is_negative(line.strip().split(" ")[1], 4) for line in file2]
            s3 = [is_negative(line.strip().split(" ")[1], 8) for line in file3]

# skoro w plikach z danymi mamy również temperatury ujemne, to logiczne, że najmniejszymi temp. będą liczby ujemne
mins1 = f"-{bin(min(s1)).lstrip('-0b')}"
mins2 = f"-{bin(min(s2)).lstrip('-0b')}"
mins3 = f"-{bin(min(s3)).lstrip('-0b')}"

print(f"{mins1}")
print(f"{mins2}")
print(f"{mins3}")

with open("wyniki_systemy.txt", "w", encoding="UTF-8") as out:
    out.write("ZADANIE 58.1\n")
    out.write(f"Minimum S1: {mins1}\n")
    out.write(f"Minimum S2: {mins2}\n")
    out.write(f"Minimum S3: {mins3}\n")