def is_contr(x, y, pixels):
    if x != 0:
        if abs(pixels[x][y] - pixels[x-1][y]) > 128:
            return True
    if x != 199:
        if abs(pixels[x][y] - pixels[x + 1][y]) > 128:
            return True
    if y != 319:
        if abs(pixels[x][y] - pixels[x][y+1]) > 128:
            return True
    if y != 0:
        if abs(pixels[x][y] - pixels[x][y-1]) > 128:
            return True
    return False

file = open("dane.txt", "r").read().split('\n') # spróbujmy z open() zamiast with ... 
pixels = [[0 for x in range(320)] for y in range(200)]
counter = 0
how_many_contr = 0
for line in file:
    if len(line.split(" ")) < 2 or len(line.split(" ")[1]) < 1:
        continue
    points = line.split(" ")
    for i in range(320):
        pixels[counter][i] = int(points[i])
    counter +=1
for i in range(200):
    for j in range(320):
        if is_contr(i, j, pixels):
            how_many_contr += 1
print(f"Pikselów kontrastujących jest: {how_many_contr}")

with open("wyniki6.txt", "a", encoding="UTF-8") as out:
    out.write("Zadanie 6.3\n")
    out.write(f"Pikselów kontrastujących jest: {how_many_contr}\n\n")