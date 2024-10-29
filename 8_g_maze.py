from collections import deque
from collections import defaultdict


def maze_options(maze, pos):
    result = []

    cur_i = pos[0]
    cur_j = pos[1]

    for i in range(cur_i + 1, len(maze)):
        if maze[i][cur_j] == 1:
            if i - 1 != cur_i:
                result.append((i - 1, cur_j))
            break
        elif maze[i][cur_j] == 2:
            result.append((i, cur_j))
            break

    for i in range(cur_i - 1, -1, -1):
        if maze[i][cur_j] == 1:
            if i + 1 != cur_i:
                result.append((i + 1, cur_j))
            break
        elif maze[i][cur_j] == 2:
            result.append((i, cur_j))
            break

    for j in range(cur_j + 1, len(maze[0])):
        if maze[cur_i][j] == 1:
            if j - 1 != cur_j:
                result.append((cur_i, j - 1))
            break
        elif maze[cur_i][j] == 2:
            result.append((cur_i, j))
            break

    for j in range(cur_j - 1, -1, -1):
        if maze[cur_i][j] == 1:
            if j + 1 != cur_j:
                result.append((cur_i, j + 1))
            break
        elif maze[cur_i][j] == 2:
            result.append((cur_i, j))
            break

    return result


def maze_steps(maze):
    visited = set()
    steps = defaultdict(int)
    queue = deque()

    start = (1, 1)
    visited.add(start)
    queue.append(start)

    while queue:
        cur_pos = queue.popleft()

        if maze[cur_pos[0]][cur_pos[1]] == 2:
            return steps[cur_pos]

        options = maze_options(maze, cur_pos)

        for pos in options:
            if pos not in visited:
                steps[pos] = steps[cur_pos] + 1
                visited.add(pos)
                queue.append(pos)


def main():
    n, m = map(int, input().split())

    maze = [[1 for _ in range(m + 2)]]

    for i in range(n):
        maze.append([1] + list(map(int, input().split())) + [1])

    maze.append([1 for _ in range(m + 2)])

    print(maze_steps(maze))


if __name__ == '__main__':
    main()
