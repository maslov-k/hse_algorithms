from collections import deque


def neighboring_vertices(adj_matrix, vertex):
    result = []

    for i in range(len(adj_matrix)):
        if adj_matrix[vertex][i]:
            result.append(i)

    return result


def restore_path(finish, prevs):
    result = []

    v = finish - 1

    while v != -1:
        result.insert(0, v + 1)
        v = prevs[v]

    return result


def min_graph_path(adj_matrix, start, finish):
    visited = [False for _i in range(len(adj_matrix))]
    queue = deque()

    visited[start - 1] = True
    queue.append(start - 1)

    paths = [-1 for _i in range(len(adj_matrix))]
    paths[start - 1] = 0
    prevs = [-1 for _i in range(len(adj_matrix))]

    while queue:
        current_v = queue.popleft()

        vertices = neighboring_vertices(adj_matrix, current_v)

        for v in vertices:
            if not visited[v]:
                paths[v] = paths[current_v] + 1
                prevs[v] = current_v
                visited[v] = True
                queue.append(v)

    return paths[finish - 1], restore_path(finish, prevs)


def main():
    n = int(input())

    adj_matrix = []

    for i in range(n):
        adj_matrix.append(list(map(int, input().split())))

    start, finish = map(int, input().split())

    length, path = min_graph_path(adj_matrix, start, finish)

    print(length)
    if length > 0:
        print(*path)


if __name__ == '__main__':
    main()
