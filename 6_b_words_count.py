from collections import defaultdict
import sys


def print_words_occurrence(words):
    count = defaultdict(int)

    for word in words:
        print(count[word], end=' ')
        count[word] += 1


def main():
    text = sys.stdin.read()

    print_words_occurrence(text.split())


if __name__ == '__main__':
    main()
