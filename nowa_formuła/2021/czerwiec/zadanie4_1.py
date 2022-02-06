with open("napisy.txt", "r") as plik:
    napisy = [linia.strip() for linia in plik]

suma = 0
for napis in napisy:
    for znak in napis:
        if znak.isdigit():
            suma += 1

print(suma)
with open("wyniki4.txt", "w") as out:
    out.write("Zadanie 4.1\n")
    out.write(f"{suma}\n\n")