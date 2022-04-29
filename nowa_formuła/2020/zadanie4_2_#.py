from collections import defaultdict


def sub_seq(word):
    counter = 1
    letters_sub = []
    counters_sub = []

    for i in range(1, len(word)):
        if word[i - 1] == word[i]:
            counter += 1
            letter = word[i - 1]
        else:
            counter = 1
            letter = word[i - 1]

        letters_sub.append(letter)
        counters_sub.append(counter)
    try:
        max_sub = max(counters_sub)
        max_seq = letters_sub[counters_sub.index(max_sub)]
    except ValueError:
        max_sub = 1
        max_seq = word
    finally:
        return f"{max_sub * max_seq} {max_sub}"

with open("pary.txt", "r") as file:
    words = [line.strip().split()[1] for line in file]

with open("wyniki4.txt", "a") as out:
    out.write("\nZADANIE 4.2\n")
    for word in words:
        print(sub_seq(word))
        out.write(f"{sub_seq(word)}\n")
