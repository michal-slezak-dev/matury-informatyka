with open("sygnaly.txt", "r", encoding="UTF-8") as file:
    signals = []

    for line in file:
        signals.append(line.strip())    # Wczytujemy sygnaly do listy, usuwamy znak końca linii
# print(signals)

# Zaczynamy od 40 sygnalu, czyli od słowa o indeksie 39(indeksujemy od 0), skok to 40(bo ma być co 40 sygnał)
# W pętli wypisujemy dziesiątą literę sygnału, tworzymy zmienną message, która będzie zawierać odczytane przesłanie
message = ""
for i in range(39, len(signals), 40):
    print(signals[i][9], end="")
    message += signals[i][9]

# Zapis do pliku
with open("wyniki4.txt", "w", encoding="UTF-8") as outputFile:
    outputFile.write("Zadanie 4.1 \n")
    outputFile.write(message + "\n")
