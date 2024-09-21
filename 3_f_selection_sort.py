def selection_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        max_j = i
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[max_j]:
                max_j = j

        arr[i], arr[max_j] = arr[max_j], arr[i]


if __name__ == '__main__':
    _n = int(input())
    _arr = list(map(int, input().split()))

    selection_sort(_arr)

    print(*_arr)
