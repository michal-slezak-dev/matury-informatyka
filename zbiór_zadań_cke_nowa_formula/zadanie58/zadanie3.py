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

counter = 1  # 1, bo pierwszy dzień to dzień rekordowy
maxs1 = [s1[0]]
maxs2 = [s2[0]]
maxs3 = [s3[0]]

for i in range(1, len(s1)):
    if s1[i] > max(maxs1) or s2[i] > max(maxs2) or s3[i] > max(maxs3):
        counter += 1
        maxs1.append(s1[i])
        maxs2.append(s2[i])
        maxs3.append(s3[i])
print(counter)

with open("wyniki_systemy.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 58.3\n")
    out.write(f"Liczba dni rekordowych: {counter}\n")


