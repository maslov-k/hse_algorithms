from collections import defaultdict


def stresses_count(word):
    return sum(1 for c in word if c.isupper())


def mistakes_count(dictionary, words):
    result = 0

    for word in words:
        stresses_vars = dictionary.get(word.lower(), '')

        stresses_cnt = stresses_count(word)

        if not stresses_vars:
            result += 1 if stresses_cnt != 1 else 0
        else:
            result += 1 if word not in stresses_vars else 0

    return result


def main():
    n = int(input())

    dictionary = defaultdict(list)

    for _i in range(n):
        word = input()
        dictionary[word.lower()].append(word)

    words = input().split()

    print(mistakes_count(dictionary, words))


if __name__ == '__main__':
    main()
