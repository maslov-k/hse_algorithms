import sys
from bisect import bisect_right, bisect_left


def value(prev_value, k, b, m):
    return (prev_value * k + b) % m


def greatest_incr_subseq_nlogn(n, a1, k, b, m):
    current_a = a1

    dynamic = [sys.maxsize for _ in range(n + 1)]
    dynamic[0] = -sys.maxsize - 1

    for i in range(n):
        d = bisect_right(dynamic, current_a)

        if d < n and dynamic[d - 1] < current_a:
            dynamic[d] = current_a

        current_a = value(current_a, k, b, m)

    return bisect_left(dynamic, sys.maxsize, 1) - 1


def main():
    n, a1, k, b, m = map(int, input().split())

    print(greatest_incr_subseq_nlogn(n, a1, k, b, m))


if __name__ == '__main__':
    main()
