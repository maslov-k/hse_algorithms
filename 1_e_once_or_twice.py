from benchmark_decorator import benchmark
from collections import defaultdict


@benchmark
def once_twice_number_my(sequence):
    d = defaultdict(int)

    for i in sequence:
        d[i] += 1

    for key, value in d.items():
        if value != 3:
            return [key, value]

    return [0, 0]


@benchmark
def once_twice_number(sequence):
    result = 0
    count = 0

    bits_count = [0 for i in range(15)]

    for num in sequence:
        i = 0
        while num > 0:
            bits_count[i] += num % 2
            num //= 2
            i += 1

    for i in range(len(bits_count)):
        bits_count[i] %= 3

    base = 2
    step = 1
    for i in range(len(bits_count)):
        if bits_count[i] != 0:
            count = bits_count[i]
            result += step
        step *= base

    return [result, count]


if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))

    print(*once_twice_number_my(seq))
