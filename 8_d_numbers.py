from collections import deque


def combine_digits(d1, d2, d3, d4):
    return d1 * 1000 + d2 * 100 + d3 * 10 + d4


def number_variants(num):
    result = []

    d1 = num // 1000
    d2 = num // 100 % 10
    d3 = num % 100 // 10
    d4 = num % 10

    if d1 != 9:
        result.append(combine_digits(d1 + 1, d2, d3, d4))
    if d4 != 1:
        result.append(combine_digits(d1, d2, d3, d4 - 1))

    result.append(combine_digits(d2, d3, d4, d1))
    result.append(combine_digits(d4, d1, d2, d3))

    return result


def restore_path(a, b, prevs):
    result = []

    v = b

    while v != a:
        result.insert(0, v)
        v = prevs[v]

    result.insert(0, v)

    return result


def number_transform(a, b):
    visited = {a: True}
    queue = deque()

    queue.append(a)

    paths = {a: 0}
    prevs = {}

    while queue:
        current_num = queue.popleft()

        variants = number_variants(current_num)

        for v in variants:
            if not visited.get(v, False):
                paths[v] = paths[current_num] + 1
                prevs[v] = current_num
                visited[v] = True
                queue.append(v)
                if v == b:
                    return restore_path(a, b, prevs)

    return []


def main():
    a = int(input())
    b = int(input())

    path = number_transform(a, b)

    for n in path:
        print(n)


if __name__ == '__main__':
    main()
