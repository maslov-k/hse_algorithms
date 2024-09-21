def insertion_sort(arr):
    cnt = 0

    for i in range(1, len(arr)):
        j = i
        swap = False
        while j > 0 and arr[j] < arr[j - 1]:
            swap = True
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        cnt += 0 if swap else 1

    return cnt


if __name__ == '__main__':
    _n = int(input())
    _arr = list(map(int, input().split()))

    count = insertion_sort(_arr)

    print(*_arr)
    print(count)
