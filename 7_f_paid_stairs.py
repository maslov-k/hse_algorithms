def paid_stairs(fares):
    if len(fares) == 1:
        return fares[0]

    prev_2 = fares[0]
    prev_1 = fares[1]

    for i in range(2, len(fares)):
        new_prev = fares[i] + min(prev_1, prev_2)
        prev_2 = prev_1
        prev_1 = new_prev

    return prev_1


def main():
    _n = int(input())
    fares = list(map(int, input().split()))

    print(paid_stairs(fares))


if __name__ == '__main__':
    main()
