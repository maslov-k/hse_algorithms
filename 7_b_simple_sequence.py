def simple_sequence(n):
    if n < 2:
        return 1

    if n % 2 == 0:
        return simple_sequence(n // 2) + simple_sequence(n // 2 - 1)
    else:
        return simple_sequence(n // 2) - simple_sequence(n // 2 - 1)


def main():
    n = int(input())

    print(simple_sequence(n))


if __name__ == '__main__':
    main()
