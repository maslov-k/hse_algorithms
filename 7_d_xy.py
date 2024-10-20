def xy(n):
    prev_1 = 2
    prev_2 = 1

    i = 1

    while i <= n:
        i += 1

        new_prev = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = new_prev

    return prev_2


def main():
    n = int(input())

    print(xy(n))


if __name__ == '__main__':
    main()
