with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]

# a) check if dobra trójka
g3 = []
g3_count = 0
for x in nums:
    for y in nums:
        for z in nums:  # sprawdzamy czy są różne i czy zgodnie z poleceniem się dzielą
            if z != y != x and y % x == 0 and z % y == 0:
                g3_count += 1
                g3.append((x, y, z))
print(g3_count)
print(g3)

with open("trójki.txt", "w") as three:
    for g3_ in g3:
        three.write(f"{g3_[0]} {g3_[1]} {g3_[2]}\n")

# b) check if dobra piątka
g5_count = 0
"""
1. sprawdzamy czy u i w są różne
2. sprawdzamy czy nie są to liczby z naszych dobrych trójek
3. sprawdzamy czy u dzieli w oraz w dzieli x
4. jeśli tak to zwiększamy licznik
"""
for g3_ in g3:
    for u in nums:  # potencjalne u i w
        for w in nums:
            if u != w and u not in g3_ and w not in g3_ and w % u == 0 and g3_[0] % w == 0:
                g5_count += 1

print(g5_count)

with open("wyniki4.txt", "a") as out:
    out.write("\n4.3\n")
    out.write(f"a) {g3_count}\nb) {g5_count}")