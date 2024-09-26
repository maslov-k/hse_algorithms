def partition_hoare(a, left, right):
    x = a[left + (right - left) // 2]

    i = left
    j = right - 1

    while True:
        while a[i] < x and i < right - 1:
            i += 1

        while a[j] > x and j > left:
            j -= 1

        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]

        i += 1
        j -= 1


def quick_sort(a, left=0, right=-1):
    if right == -1:
        right = len(a)

    while left < right - 1:
        m = partition_hoare(a, left, right)

        if m - left < right - m:
            quick_sort(a, left, m)
            left = m + 1
        else:
            quick_sort(a, m + 1, right)
            right = m


if __name__ == '__main__':
    _n = int(input())
    _arr = list(map(int, input().split()))

    quick_sort(_arr)
    quick_sort(_arr)

    print(*_arr)
