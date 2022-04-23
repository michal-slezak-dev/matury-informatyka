with open("dane.txt", "r") as file:
    pixels_rows = [list(map(int, line.strip().split())) for line in file]

how_many_to_del = 0
for row in pixels_rows:
    for i in range(len(row)):
        if row[i] != row[len(row) - i - 1]:
            how_many_to_del += 1
            break
print(f"Najmniejsza liczba wierszy, jaką należy usunąć, aby obraz miał pionową oś symetrii wynosi: {how_many_to_del}")

with open("wyniki6.txt", "a", encoding="UTF-8") as out:
    out.write("Zadanie 6.2\n")
    out.write(f"Najmniejsza liczba wierszy, jaką należy usunąć, aby obraz miał pionową oś symetrii wynosi: {how_many_to_del}\n\n")