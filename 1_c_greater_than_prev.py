def greater_count(sequence):
    result = 0

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            result += 1
    return result


if __name__ == '__main__':
    seq = []

    while True:
        n = int(input())
        if n == 0:
            break
        seq.append(n)

    print(greater_count(seq))
