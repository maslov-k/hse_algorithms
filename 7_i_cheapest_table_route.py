def cheapest_table_route(table):
    n = len(table)
    m = len(table[0])

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                table[i][j] = table[i][j] + table[i][j - 1]
            elif j == 0:
                table[i][j] = table[i][j] + table[i - 1][j]
            else:
                table[i][j] = table[i][j] + min(table[i][j - 1], table[i - 1][j])

    return table[-1][-1]


def main():
    n, m = map(int, input().split())

    table = []

    for _i in range(n):
        table.append(list(map(int, input().split())))

    print(cheapest_table_route(table))


if __name__ == '__main__':
    main()
