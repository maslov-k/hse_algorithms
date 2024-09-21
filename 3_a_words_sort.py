class SortedWords:
    def __init__(self):
        self.words = []

    def insert_index(self, word):
        left = 0
        right = len(self.words)

        while left < right:
            m = left + (right - left) // 2

            if len(self.words[m]) > len(word):
                right = m
            else:
                left = m + 1

        return right

    def add_word(self, word):
        self.words.insert(self.insert_index(word), word)

    def print_words(self):
        for word in self.words:
            print(word)


if __name__ == '__main__':
    sorted_words = SortedWords()

    _n = int(input())

    for i in range(_n):
        sorted_words.add_word(input())

    sorted_words.print_words()
