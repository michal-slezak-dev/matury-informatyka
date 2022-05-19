with open("sygnaly.txt", "r") as file:
    signals = []
    for line in file:
        signals.append(line.strip())

answers_strings = []
for signal in signals:
    distances = []  # ta lista przechowuje odległości między literami w danym słowie

    for i in range(len(signal)):
        for j in range(1, len(signal)):
            distances.append(abs(ord(signal[i]) - ord(signal[j])))  # wartość bezwzględna z kodów ascii poszczególnych liter (ich odległość)

    if max(distances) <= 10:  # lub sorted(distances, reverse=True)[0] <= 10
        print(signal)
        answers_strings.append(signal)

with open("wyniki4.txt", "a", encoding="UTF-8") as out:
    out.write("ZADANIE 4.3\n")
    for string in answers_strings:
        out.write(f"{string}\n")