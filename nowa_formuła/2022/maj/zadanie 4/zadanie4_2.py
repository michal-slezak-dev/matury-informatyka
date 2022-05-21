def prime_factors(n):
    factors = []

    k = 2
    while n != 1:
        while n % k == 0:
            factors.append(k)
            n //= k
        k += 1
    return factors


with open("liczby.txt", "r") as file:
    nums = [int(line.strip()) for line in file]


# a) słownik zabiera w kluczach liczba a w wartościach ilość czynników pierwszych danej liczby
num_pf = {num: len(prime_factors(num)) for num in nums}

max_num_pf = max(num_pf.values())
for num in num_pf:
    if num_pf[num] == max_num_pf:
        max_num = num

# b) słownik zabiera w kluczach liczba a w wartościach ilość czynników pierwszych danej liczby, ale jest to set,
num_dpf = {num: len(list(set(prime_factors(num)))) for num in nums}  # więc usuwa zduplikowane czynniki pierwsze
max_num_dpf = max(num_dpf.values())
for num in num_dpf:
    if num_dpf[num] == max_num_dpf:
        max_dnum = num

print(max_num, max_num_pf, max_dnum, max_num_dpf)

with open("wyniki4.txt", "a") as out:
    out.write("\n4.2\n")
    out.write(f"{max_num} {max_num_pf} {max_dnum} {max_num_dpf}\n")