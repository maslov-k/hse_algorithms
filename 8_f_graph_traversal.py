from collections import deque


def neighboring_vertices(adj_matrix, vertex):
    result = []

    for i in range(len(adj_matrix)):
        if adj_matrix[vertex][i]:
            result.append(i)

    return result


def component_size(adj_matrix, vertex):
    result = 0

    visited = [False for _ in range(len(adj_matrix))]
    queue = deque()

    visited[vertex] = True
    queue.append(vertex)

    while queue:
        result += 1
        current_v = queue.popleft()

        vertices = neighboring_vertices(adj_matrix, current_v)

        for v in vertices:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return result


def main():
    n, s = map(int, input().split())

    adj_matrix = []

    for i in range(n):
        adj_matrix.append(list(map(int, input().split())))

    print(component_size(adj_matrix, s - 1))


if __name__ == '__main__':
    main()
