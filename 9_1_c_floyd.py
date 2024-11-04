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

    adj_matrix = []

    for i in range(n):
        adj_matrix.append(list(map(int, input().split())))

    distances = floyd(adj_matrix)

    for i in distances:
        print(*i)


if __name__ == '__main__':
    main()
