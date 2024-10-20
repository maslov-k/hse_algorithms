def table_routes(n, m):
    dynamic = [[1 for _j in range(m)] for _i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            dynamic[i][j] = dynamic[i - 1][j] + dynamic[i][j - 1]

    return dynamic[-1][-1]


def main():
    n, m = map(int, input().split())

    print(table_routes(n, m))


if __name__ == '__main__':
    main()
