import sys


def floyd(adj_matrix):
    n = len(adj_matrix)

    distances = [[sys.maxsize] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif adj_matrix[i][j] != 0:
                distances[i][j] = adj_matrix[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


def main():
    n = int(input())
    m = int(input())

    adj_matrix = [[0] * n for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        adj_matrix[a][b] = w

    distances = floyd(adj_matrix)

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = distances[i][j]
                print(i, j, distance if distance < sys.maxsize else -1)


if __name__ == '__main__':
    main()
