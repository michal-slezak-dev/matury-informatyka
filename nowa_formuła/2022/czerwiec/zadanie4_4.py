def count_nums_occurance(n, nums):
    """W zaleznosci od podpunktu to sprawdzamy ile liczb wystepuje dokladnie n razy"""
    counter = 0
    num_occurance = {num: nums.count(num) for num in nums}

    if n == 2:
        for num in num_occurance:
            if num_occurance[num] == 2:
                counter += 1
    if n == 3:
        for num in num_occurance:
            if num_occurance[num] == 3:
                counter += 1

    return counter

with open("liczby.txt", "r") as file:
    nums = [line.strip() for line in file]

# a)
num_of_diff_nums = len(set(nums))

# b)
counter2 = count_nums_occurance(2, nums)

# c)
counter3 = count_nums_occurance(3, nums)


with open("wyniki4.txt", "a", encoding='UTF-8') as out:
    out.write("ZADANIE 4.4:\n")
    out.write(f"{num_of_diff_nums} {counter2} {counter3}")