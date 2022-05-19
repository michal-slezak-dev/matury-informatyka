with open("sygnaly.txt", "r") as file:
    signals = []
    for line in file:
        signals.append(line.strip())

# co czterdzieste słowo i dziesiąty znak
msg = ""
for i in range(39, len(signals), 40):
    msg += signals[i][9]

print(msg)

with open("wyniki4.txt", "w", encoding="UTF-8") as out:
    out.write("ZADANIE 4.1\n")
    out.write(f"{msg}\n\n")