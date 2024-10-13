import sys
from collections import defaultdict
from functools import cmp_to_key


def compare_pairs(left, right):
    if left[1] < right[1]:
        return 1
    elif left[1] > right[1]:
        return -1
    else:
        if left[0] > right[0]:
            return 1
        elif left[0] < right[0]:
            return -1
        else:
            return 0


def main():
    freqs = defaultdict(int)

    for line in sys.stdin:
        for word in line.split():
            if word:
                freqs[word] += 1

    for [word, count] in sorted(freqs.items(), key=cmp_to_key(compare_pairs)):
        print(word)


if __name__ == '__main__':
    main()
