def is_graph_complete(adj_matrix):
    result = True

    for i in range(len(adj_matrix)):
        for j in range(i + 1, len(adj_matrix)):
            if not adj_matrix[i][j]:
                result = False

    return result


def main():
    n, m = map(int, input().split())

    adj_matrix = [[False for _i in range(n)] for _j in range(n)]

    for _i in range(m):
        v1, v2 = map(int, input().split())
        adj_matrix[v1 - 1][v2 - 1] = True
        adj_matrix[v2 - 1][v1 - 1] = True

    print('YES' if is_graph_complete(adj_matrix) else 'NO')


if __name__ == '__main__':
    main()
