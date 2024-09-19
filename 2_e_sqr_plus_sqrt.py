import math

EPSILON = 0.0000001


def is_equal(x, c):
    return abs(x - c) < EPSILON


def y_result(x):
    return x * x + math.sqrt(x)


def sqr_plus_sqrt(c):
    left = 0
    right = 100000

    while True:
        x = left + (right - left) / 2
        y = y_result(x)
        if is_equal(y, c):
            return x
        elif y < c:
            left = x
        else:
            right = x


if __name__ == '__main__':
    _c = float(input())

    print(sqr_plus_sqrt(_c))
