with open("sygnaly.txt", "r", encoding="UTF-8") as file:
    signals = []

    for line in file:
        signals.append(line.strip())  # Wczytujemy sygnaly do listy, usuwamy znak końca linii
# print(signals)

# W pętli tworzymy zmienną less_than_10, która w zależności od odległości- będzie przechowywać True lub False
# Tworzymy też listę, która będzie przechowywać odległości liter w danym słowie
# Odległości danych liter możemy obliczyć odejmując od siebie kody ascii tych liter
# Robimy też 2 pętle for i in range... i for j in range...
# Porównujemy 2 litery, więc pętla z i będzie odpowiadać za naszą 1 literę, pętla j za te kolejne
# Tworzymy zmienną dist, która będzie przechowywać odległość między 2 literami
# Jeśli odległość między danymi literami jest większa od 10 to ustawiamy less_than_10 na False i robimy break, aby już nie sprawdzać innych liter z tą aktualną
# Potem sprawdzamy też jeśli less_than_10 jest ma wartość False to też robimy break, który spowoduje to, że przejdziemy do innego słowa
# Jeśli natomiast less_than_10 jest ma wartość True to wypisujemy to słowo, ponieważ spełnia ono warunek określony w poleceniu zadania

answers_words = []

print("Te słowa to: ")

for signal in signals:
    less_than_10 = True
    for i in range(len(signal)):
        for j in range(i + 1, len(signal)):
            dist = abs(ord(signal[j]) - ord(signal[i]))
            # print(dist)

            if dist > 10:
                less_than_10 = False
                break

        if less_than_10 == False:
            break

    if less_than_10 == True:
        print(signal)
        answers_words.append(signal)

# Tutaj standardowo zapis do pliku

with open("wyniki4.txt", "a", encoding="UTF-8") as outputFile:
    outputFile.write("\nZadanie 4.3 \n")
    outputFile.write("Te słowa to: \n")

    for word in answers_words:
        outputFile.write(str(word) + "\n")
