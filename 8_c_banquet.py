from collections import deque


def neighboring_vertices(adj_matrix, vertex):
    result = []

    for i in range(len(adj_matrix)):
        if adj_matrix[vertex][i]:
            result.append(i)

    return result


def graph_parts(adj_matrix):
    visited = [False for _i in range(len(adj_matrix))]

    parts = {}

    for i in range(len(adj_matrix)):
        if not visited[i]:
            queue = deque()

            parts[i] = 0
            visited[i] = True
            queue.append(i)

            while queue:
                current_v = queue.popleft()

                vertices = neighboring_vertices(adj_matrix, current_v)

                for v in vertices:
                    if visited[v]:
                        if parts[v] == parts[current_v]:
                            return {}
                    else:
                        queue.append(v)
                        parts[v] = 1 - parts[current_v]
                        visited[v] = True

    return parts


def main():
    n, m = map(int, input().split())

    adj_matrix = [[False for _i in range(n)] for _j in range(n)]

    for _i in range(m):
        v1, v2 = map(int, input().split())
        adj_matrix[v1 - 1][v2 - 1] = True
        adj_matrix[v2 - 1][v1 - 1] = True

    parts = graph_parts(adj_matrix)

    bipartite = len(parts) > 0

    print('YES' if bipartite else 'NO')

    if bipartite:
        for i in range(n):
            if parts.get(i, 0) == 0:
                print(i + 1, end=' ')


if __name__ == '__main__':
    main()
