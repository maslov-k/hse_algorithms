from functools import lru_cache


@lru_cache
def knight_options(n, m):
    if n == 1 and m == 1:
        return 1
    elif n < 1 or m < 1:
        return 0

    return knight_options(n - 1, m - 2) + knight_options(n - 2, m - 1)


def main():
    n, m = map(int, input().split())

    print(knight_options(n, m))


if __name__ == '__main__':
    main()
