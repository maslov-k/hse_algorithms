def stones(weights):
    full_sum = sum(weights)

    return full_sum - 2 * stones_recursion(weights, full_sum // 2, len(weights))


def stones_recursion(weights, w, i):
    if w <= 0 or i <= 0:
        return 0

    if weights[i - 1] > w:
        return stones_recursion(weights, w, i - 1)

    return max(stones_recursion(weights, w, i - 1), stones_recursion(weights, w - weights[i - 1], i - 1) + weights[i - 1])


def main():
    n = int(input())
    weights = list(map(int, input().split()))

    print(stones(weights))


if __name__ == '__main__':
    main()
