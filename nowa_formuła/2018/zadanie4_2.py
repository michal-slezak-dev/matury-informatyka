with open("sygnaly.txt", "r", encoding="UTF-8") as file:
    signals = []

    for line in file:
        signals.append(line.strip())    # Wczytujemy sygnaly do listy, usuwamy znak końca linii
# print(signals)

# Tworzymy słownik, który będzie przechowywać słowo w kluczach i liczbę różnych liter w tym słowie w wartościach
uniq_words = {}


# Dzięki temu, że tworzymy set - to automatycznie odrzuci nam powtórzenia danych liter i długość seta będzie równa liczbie różnych liter
# Na końcu dodajemy do słownika dane słowo i długość seta
for signal in signals:
    uniq_number_of_letters = set()
    for letter in signal:
        uniq_number_of_letters.add(letter)

    uniq_words.update({signal: len(uniq_number_of_letters)})
# print(uniq_words)

# Tworzymy zmienną, która przechowuje największą liczbę różnych liter, która pojawiła się w jakimś słowie
maxNumberOfUniqLetters = max(uniq_words.values())

# Tutaj w pętli będziemy sprawdzać czy wartość jest równa największej liczbie różnych liter
# Jeśli tak to deklarujemy zmienną, do której przypiszemy to słowo i robimy breaka, bo jeśli jest więcej słów o największej liczbie różnych liter
# to mamy wypisać to pierwsze, więc dlatego robimy break
for word in uniq_words:
    if uniq_words[word] == maxNumberOfUniqLetters:
        wordWithMaxNumberOfUniqLetters = word
        break
# print(wordWithMaxNumberOfUniqLetters)

print(f'Słowo o największej liczbie różnych liter to(słowo liczba różnych liter): {wordWithMaxNumberOfUniqLetters}, ma ono {maxNumberOfUniqLetters} różnych liter.')

# Zapis do pliku
with open("wyniki4.txt", "a", encoding="UTF-8") as outputFile:
    outputFile.write("\nZadanie 4.2 \n")
    outputFile.write("Słowo o największej liczbie różnych liter oraz liczba różnych liter: \n")
    outputFile.write(wordWithMaxNumberOfUniqLetters + " " + str(maxNumberOfUniqLetters) + "\n")
