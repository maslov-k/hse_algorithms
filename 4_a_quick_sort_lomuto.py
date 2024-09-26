def partition_lomuto(a, left, right):
    x = a[right - 1]
    j = left

    for i in range(left, right - 1):
        if a[i] <= x:
            a[j], a[i] = a[i], a[j]
            j += 1

    a[right - 1], a[j] = a[j], a[right - 1]

    return j


def quick_sort(a, left=0, right=-1, rec_count=0):
    if right == -1:
        right = len(a)

    while left < right - 1:
        m = partition_lomuto(a, left, right)
        if m - left < right - m:
            rec_count = quick_sort(a, left, m, rec_count + 1)
            left = m + 1
        else:
            rec_count = quick_sort(a, m + 1, right, rec_count + 1)
            right = m

    return rec_count


if __name__ == '__main__':
    _n = int(input())
    _arr = list(map(int, input().split()))

    recursions_count = quick_sort(_arr)

    print(recursions_count - 1 if recursions_count > 0 else 0)
    print(*_arr)
