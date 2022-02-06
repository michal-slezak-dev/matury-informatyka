with open("napisy.txt", "r") as plik:
    napisy = [linia.strip() for linia in plik]

pozycja = 0
haslo = ""
for i in range(19, len(napisy), 20):
    haslo += napisy[i][pozycja]
    pozycja += 1

print(haslo)
with open("wyniki4.txt", "a") as out:
    out.write("Zadanie 4.2\n")
    out.write(f"{haslo}\n\n")
