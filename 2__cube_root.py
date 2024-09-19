EPSILON = 0.0000000000000001


def is_zero(x):
    return abs(x) < EPSILON


def equation_y(a, b, c, d, x):
    return a * x * x * x + b * x * x + c * x + d


def cube_root(a, b, c, d):
    left = -2000
    right = 2000
    cnt = 0
    while True:
        cnt += 1
        x = left + (right - left) / 2
        y = equation_y(a, b, c, d, x)
        if is_zero(y):
            return x
        elif y < 0:
            left = x
        else:
            right = x


if __name__ == '__main__':
    _a, _b, _c, _d = map(int, input().split())

    print(cube_root(_a, _b, _c, _d))
