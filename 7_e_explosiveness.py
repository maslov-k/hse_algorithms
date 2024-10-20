def explosiveness(n):
    prev_1 = 3
    prev_2 = 1

    i = 1

    while i <= n:
        i += 1

        new_prev = prev_1 * 2 + prev_2 * 2
        prev_2 = prev_1
        prev_1 = new_prev

    return prev_2


def main():
    n = int(input())

    print(explosiveness(n))


if __name__ == '__main__':
    main()
