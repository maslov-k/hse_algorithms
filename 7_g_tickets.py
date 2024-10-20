def tickets(times):
    if len(times) == 1:
        return times[0][0]

    prev_3 = times[-1][0]
    prev_2 = min(prev_3 + times[-2][0], times[-2][1])

    if len(times) == 2:
        return prev_2

    prev_1 = min(times[-3][0] + prev_2, times[-3][1] + prev_3, times[-3][2])

    for i in range(len(times) - 4, -1, -1):
        new_prev = min(times[i][0] + prev_1, times[i][1] + prev_2, times[i][2] + prev_3)
        prev_3, prev_2, prev_1 = prev_2, prev_1, new_prev

    return prev_1


def main():
    n = int(input())
    times = []

    for _i in range(n):
        times.append(list(map(int, input().split())))

    print(tickets(times))


if __name__ == '__main__':
    main()
