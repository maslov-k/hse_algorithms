def knapsack(max_weight, weights, costs):
    dynamic = [[0 for _j in range(len(weights) + 1)] for _i in range(max_weight + 1)]

    for i in range(1, len(weights) + 1):
        for w in range(1, max_weight + 1):
            dynamic[w][i] = dynamic[w][i - 1]
            if weights[i - 1] <= w:
                dynamic[w][i] = max(dynamic[w][i], dynamic[w - weights[i - 1]][i - 1] + costs[i - 1])

    return dynamic[-1][-1]


def main():
    _n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    print(knapsack(m, weights, costs))


if __name__ == '__main__':
    main()
