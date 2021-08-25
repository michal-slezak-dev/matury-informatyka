with open("sygnaly.txt", "r", encoding="UTF-8") as file:
    signals = []

    for line in file:
        signals.append(line.strip())  # Wczytujemy sygnaly do listy, usuwamy znak końca linii
# print(signals)

# W pętli tworzymy słownik, który jako klucze będzie miał słowa, a jako wartości  - odległości liter
# Odległości danych liter możemy obliczyć odejmując od siebie kody ascii tych liter
# Tworzymy też listę, która będzie przechowywać odległości liter w danym słowie
# Robimy też 2 pętle for i in range... i for j in range...
# Porównujemy 2 litery, więc pętla z i będzie odpowiadać za naszą 1 literę, pętla j za te kolejne
# Tworzymy zmienną dist, która będzie przechowywać dystans między danymi literami, dodajemy ten dystans do listy distance
# Poza pętlami, które porównują litery dodajemy do słownika słowo(jako klucz) oraz listę z odległościami między danymi literami
# Następnie tworzymy kolejną pętlę, która będzie sprawdzać nam te odległości
# W tej pętli sortujemy malejąco listy z odległościami między danymi literami
# Z racji tego, że posortowaliśmy malejąco to w liście na indeksie 0 będziae największa odległość między danymi literami
# Potem w tej samej pętli sprawdzamy czy wartość listy o indeksie 0 jest większa od 10, jeśli tak - to zatrzymujemy pętlę i przechodzimy do kolejnego słowa
# Jeśli jest mniejsza lub równa 10 to wypisujemy to słowo
#  Aby zapisać odpowiedzi do pliku - tworzymy też listę, która będzie zawierać te poprawne słowa

answers_words = []

print("Te słowa to")

for signal in signals:
    distances = {}
    distance = []
    for i in range(len(signal)):
        for j in range(1, len(signal)):
            dist = abs(ord(signal[j]) - ord(signal[i]))
            distance.append(dist)
    # print(distance)
    distances.update({signal: distance})
    # print(distances)

    for word in distances:
        distances[word] = sorted(distances[word], reverse=True)

        if distances[word][0] > 10:
            break
        else:
            print(word)
            answers_words.append(word)

# Na koniec zapisujemy do pliku
with open("wyniki4.txt", "a", encoding="UTF-8") as outputFile:
    outputFile.write("\nZadanie 4.3 \n")
    outputFile.write("Te słowa to: \n")

    for word in answers_words:
        outputFile.write(str(word) + "\n")
