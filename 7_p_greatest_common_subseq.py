def gcs_answer(dynamic, s1, s2):
    s1_subseq_ind = []
    s2_subseq_ind = []

    i = len(dynamic) - 1
    j = len(dynamic[0]) - 1

    while dynamic[i][j] != 0:
        if s2[i - 1] == s1[j - 1]:
            s1_subseq_ind.insert(0, j)
            s2_subseq_ind.insert(0, i)

            i -= 1
            j -= 1
        elif dynamic[i - 1][j] > dynamic[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return [s1_subseq_ind, s2_subseq_ind]


def greatest_common_subseq(s1, s2):
    dynamic = [[0 for _j in range(len(s1) + 1)] for _i in range(len(s2) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                dynamic[i][j] = dynamic[i - 1][j - 1] + 1
            else:
                dynamic[i][j] = max(dynamic[i - 1][j], dynamic[i][j - 1])

    return dynamic


def main():
    s1 = input()
    s2 = input()

    dynamic = greatest_common_subseq(s1, s2)

    [s1_subseq_ind, s2_subseq_ind] = gcs_answer(dynamic, s1, s2)

    print(dynamic[-1][-1])
    print(*s1_subseq_ind)
    print(*s2_subseq_ind)


if __name__ == '__main__':
    main()
