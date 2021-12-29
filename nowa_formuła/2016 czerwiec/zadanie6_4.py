def onlyNum(num):
    num = ''.join(list(num)[:len(num) - 1]) # pozbywamy się ostatniej cyfry kodu
    return num

with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

sum = 0
for num in nums:
    if num[-1] == "8":
        num = onlyNum(num)
        sum += int(num, 8)

print(sum)