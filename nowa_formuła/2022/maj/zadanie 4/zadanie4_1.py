with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

counter = 0  # zlicza ilość liczb spełniających warunek
ans = []  # zawiera te liczby spełniające warunek
for num in nums:
    if num[0] == num[-1]:
        counter += 1
        ans.append(num)

print(counter, ans[0])

with open("wyniki4.txt", "w") as out:
    out.write("4.1\n")
    out.write(f"{counter} {ans[0]}\n")

