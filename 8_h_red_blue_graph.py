def neighboring_vertices(adj_matrix, vertex):
    result = []

    for i in range(len(adj_matrix)):
        if adj_matrix[vertex][i]:
            result.append(i)

    return result


def dfs(adj_matrix, colors, v=0):
    colors[v] = 1

    for u in neighboring_vertices(adj_matrix, v):
        if colors[u] == 0:
            dfs(adj_matrix, colors, u)
        elif colors[u] == 1:
            return True

    colors[v] = 2

    return False


def has_cycle(adj_matrix):
    colors = [0 for _ in range(len(adj_matrix))]

    for i in range(len(adj_matrix)):
        if dfs(adj_matrix, colors, i):
            return True

    return False


def main():
    n = int(input())

    adj_matrix = [[False] * n for _ in range(n)]

    for i in range(n - 1):
        for j, c in enumerate(input()):
            if c == 'R':
                adj_matrix[i][j + i + 1] = True
            elif c == 'B':
                adj_matrix[j + i + 1][i] = True

    print('NO' if has_cycle(adj_matrix) else 'YES')


if __name__ == '__main__':
    main()
