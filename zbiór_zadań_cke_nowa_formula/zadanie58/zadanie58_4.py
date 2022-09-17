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

def num_ceil(num):
    num = str(num).split(".")
    if float(num[1]) > 0:
        return int(num[0]) + 1
    return int(num[0])

with open("dane_systemy1.txt", "r") as file1:
    s1 = [is_negative(line.strip().split(" ")[1], 2) for line in file1]

# jumps = []
# for i in range(len(s1)):
#     for j in range(i + 1, len(s1)):
#         r = (s1[i] - s1[j]) ** 2
#         temp_j = num_ceil(r/abs(i - j))
#
#         jumps.append(temp_j)

jumps = [num_ceil(((s1[i] - s1[j]) ** 2)/abs(i - j)) for i in range(len(s1)) for j in range(i + 1, len(s1))]

print(max(jumps))

with open("wyniki_systemy.txt", "a", encoding="UTF-8") as out:
    out.write("\nZADANIE 58.4\n")
    out.write(f"Największy skok temperatury w stacji S1: {max(jumps)}\n")