def ball_options(n):
    prevs = [4, 2, 1]

    if n == 0:
        return 0
    elif n < 3:
        return prevs[3 - n]

    i = 3

    while i < n:
        new_prev = sum(prevs)
        prevs[2] = prevs[1]
        prevs[1] = prevs[0]
        prevs[0] = new_prev

        i += 1

    return prevs[0]


def main():
    n = int(input())

    print(ball_options(n))


if __name__ == '__main__':
    main()
