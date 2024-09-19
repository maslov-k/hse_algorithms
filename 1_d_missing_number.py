def missing_number(sequence):
    max_value = len(sequence) + 1

    real_sum = sum(sequence)
    full_sum = int((1 + max_value) * max_value / 2)

    return full_sum - real_sum


if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))

    print(missing_number(seq))
