with open("sygnaly.txt", "r") as file:
    signals = []
    for line in file:
        signals.append(line.strip())

# słownik: klucze -> słowa, wartości -> ilość różnych liter
str_and_num_of_diff_l = {}
for signal in signals:
    str_and_num_of_diff_l.update({signal: len(set(signal))})

max_num_of_diff_l = max(str_and_num_of_diff_l.values())  # wyłaniamy największą liczbę różnych liter

# wypisujemy największą ilość różnych liter i pierwsze słowo, które ma taką ilość
print(max_num_of_diff_l)
for string in str_and_num_of_diff_l:
    if str_and_num_of_diff_l[string] == max_num_of_diff_l:
        print(string)
        max_string = string
        break

with open("wyniki4.txt", "a", encoding="UTF-8") as out:
    out.write("ZADANIE 4.2\n")
    out.write(f"{max_num_of_diff_l}\n")
    out.write(f"{max_string}\n\n")
