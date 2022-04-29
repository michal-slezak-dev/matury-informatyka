def is_smaller(pair1, pair2):
    num1, num2 = int(pair1[0]), int(pair2[0])
    word1, word2 = pair1[1], pair2[1]

    return -1 * num1 < num2 or (-1 * num1 == num2 and word1 < word2)

with open("pary.txt", "r") as file:
    nums_words = [tuple(line.strip().split()) for line in file if int(line.strip().split()[0]) == len(line.strip().split()[1])]

for i in range(len(nums_words)):
    for j in range(1, len(nums_words)):
        if is_smaller(nums_words[i], nums_words[j]):
            the_smallest = nums_words[i]  # sprawdzamy kolejne pary [i]

with open("wyniki4.txt", "a") as out:
    out.write("\nZADANIE 4.3\n")
    print(f"{the_smallest[0]} {the_smallest[1]}")
    out.write(f"{the_smallest[0]} {the_smallest[1]}")