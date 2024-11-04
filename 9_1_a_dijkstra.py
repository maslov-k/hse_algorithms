import sys


def neighboring_vertices(adj_matrix, vertex):
    result = []

    for j in range(len(adj_matrix)):
        w = adj_matrix[vertex][j]
        if w > 0:
            result.append((j, w))

    return result


def dijkstra(adj_matrix, start, finish):
    distances = [sys.maxsize for _ in range(len(adj_matrix))]
    distances[start] = 0
    unvisited = [i for i in range(len(adj_matrix))]

    while unvisited:
        current_v = min(unvisited, key=lambda x: distances[x])
        unvisited.remove(current_v)

        vertices = neighboring_vertices(adj_matrix, current_v)

        for v, w in vertices:
            dist = distances[current_v] + w
            if dist < distances[v]:
                distances[v] = dist

    return distances[finish]


def main():
    n, s, f = map(int, input().split())

    adj_matrix = []

    for i in range(n):
        adj_matrix.append(list(map(int, input().split())))

    distance = dijkstra(adj_matrix, s - 1, f - 1)

    print(distance if distance < sys.maxsize else -1)


if __name__ == '__main__':
    main()
