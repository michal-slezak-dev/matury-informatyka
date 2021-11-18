with open("sygnaly.txt", "r", encoding="UTF-8") as file:
    signals = []

    for line in file:
        signals.append(line.strip())    # Wczytujemy sygnaly do listy, usuwamy znak końca linii
# print(signals)

# Tworzymy słownik, który będzie przechowywać słowo w kluczach i liczbę różnych liter w tym słowie w wartościach
unique_words = {}


# Dzięki temu, że tworzymy set - to automatycznie odrzuci nam powtórzenia danych liter i długość seta będzie równa liczbie różnych liter
# Na końcu dodajemy do słownika dane słowo i długość seta
for signal in signals:
    unique_number_of_letters = set()
    for letter in signal:
        unique_number_of_letters.add(letter)

    unique_words.update({signal: len(unique_number_of_letters)})
# print(unique_words)

# Tworzymy zmienną, która przechowuje największą liczbę różnych liter, która pojawiła się w jakimś słowie
maxNumberOfUniqueLetters = max(unique_words.values())

# Tutaj w pętli będziemy sprawdzać czy wartość jest równa największej liczbie różnych liter
# Jeśli tak to deklarujemy zmienną, do której przypiszemy to słowo i robimy breaka, bo jeśli jest więcej słów o największej liczbie różnych liter
# to mamy wypisać to pierwsze, więc dlatego robimy break
for word in unique_words:
    if unique_words[word] == maxNumberOfUniqueLetters:
        wordWithMaxNumberOfUniqueLetters = word
        break
# print(wordWithMaxNumberOfUniqLetters)

print(f'Słowo o największej liczbie różnych liter to(słowo liczba różnych liter): {wordWithMaxNumberOfUniqueLetters}, ma ono {maxNumberOfUniqueLetters} różnych liter.')

# Zapis do pliku
with open("wyniki4.txt", "a", encoding="UTF-8") as outputFile:
    outputFile.write("\nZadanie 4.2 \n")
    outputFile.write("Słowo o największej liczbie różnych liter oraz liczba różnych liter: \n")
    outputFile.write(wordWithMaxNumberOfUniqueLetters + " " + str(maxNumberOfUniqueLetters) + "\n")