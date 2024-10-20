def greatest_mult_subseq(a):
    dynamic = [1]

    for i in range(1, len(a)):
        max_prev_subseq = 0
        for j in range(i):
            if a[i] % a[j] == 0:
                max_prev_subseq = max(max_prev_subseq, dynamic[j])

        dynamic.append(max_prev_subseq + 1)

    return max(dynamic)


def main():
    _n = int(input())
    a = list(map(int, input().split()))

    print(greatest_mult_subseq(a))


if __name__ == '__main__':
    main()
