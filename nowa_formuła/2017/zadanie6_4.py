with open("dane.txt", "r") as file:
    pixels_rows = [list(map(int, line.strip().split())) for line in file]

    pixels_cols = [[] for _ in range(len(pixels_rows[0]))]

    for row in pixels_rows:
        k = 0
        for i in range(len(row)):
            pixels_cols[k].append(row[k])
            k += 1

longest_sub = []
for col in pixels_cols:
    counter = 1
    for i in range(1, len(col)):
        if col[i - 1] == col[i]:
            counter += 1
        else:
            counter = 1
        longest_sub.append(counter)
print(f"Najdłuższa taka linia pionowa wynosi: {max(longest_sub)}")

with open("wyniki6.txt", "a", encoding="UTF-8") as out:
    out.write("Zadanie 6.4\n")
    out.write(f"Najdłuższa taka linia pionowa wynosi: {max(longest_sub)}")
