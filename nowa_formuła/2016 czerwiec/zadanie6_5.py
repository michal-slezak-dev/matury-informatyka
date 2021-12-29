def onlyNum(num):
    num = ''.join(list(num)[:len(num) - 1]) # pozbywamy się ostatniej cyfry kodu
    return num

def convert(num, base):
    return int(num, base) # konwersja na system dziesiętny

with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

decimals = [] # przechowuje przekonwertowane na system dziesiętny liczby z kodów
codes = [] # przechowuje kody odpowiednich liczb przekonwertowanych na system dziesiętny
for num in nums:
    decimalNum = convert(onlyNum(num), int(num[-1])) # nasza liczba z kodu w systemie dziesiętnym
    numCode = num # kod

    decimals.append(decimalNum)
    codes.append(numCode)

maxNum = max(decimals) # wyznaczamy maksimum z przekonwertowanych kodów
maxNumIndex = decimals.index(maxNum) # wyznaczamy indeks maksimum, bo jest taki sam co kodu w liście codes
maxNumCode = codes[maxNumIndex] # wyznaczamy kod minimum

minNum = min(decimals) #wyznaczamy minimum z przekonwertowanych kodów
minNumIndex = decimals.index(minNum) # wyznaczamy indeks maksimum, bo jest taki sam co kodu w liście codes
minNumCode = codes[minNumIndex] # wyznaczamy kod minimum

print(f"Maks:\n{maxNumCode} {maxNum}\nMin:\n{minNumCode} {minNum}")