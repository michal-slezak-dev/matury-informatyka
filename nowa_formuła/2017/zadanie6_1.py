with open("dane.txt", "r") as file:
    pixels_rows = [list(map(int, line.strip().split())) for line in file]

pixels = [pixel for row in pixels_rows for pixel in row]
print(f"Najjaśniejszy: {max(pixels)}\nNajciemniejszy: {min(pixels)}")

with open("wyniki6.txt", "w", encoding="UTF-8") as out:
    out.write("Zadanie 6.1\n")
    out.write(f"Najjaśniejszy: {max(pixels)}\nNajciemniejszy: {min(pixels)}\n\n")