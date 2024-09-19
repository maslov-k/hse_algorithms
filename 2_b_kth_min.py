def new_first_row_index(arr, rows_order):
    left = 0
    right = len(rows_order) - 1

    x = arr[rows_order[0]][0]

    while left < right:
        m = left + (right - left) // 2

        if arr[rows_order[m]][0] < x:
            left = m + 1
        else:
            right = m

    return left


def k_th_min(arr, k):
    rows_order = [i for i in range(len(arr))]

    min_cnt = 1

    while min_cnt < k:
        first_row = rows_order[0]
        arr[first_row].pop(0)

        if len(arr[first_row]) == 0:
            rows_order.pop(0)
        else:
            new_index = new_first_row_index(arr, rows_order)
            if new_index != 0:
                rows_order.insert(new_index, rows_order.pop(0))

        min_cnt += 1

    return arr[rows_order[0]][0]


if __name__ == '__main__':
    _n, _k = map(int, input().split())

    _arr = []

    for _i in range(_n):
        _arr.append(list(map(int, input().split())))

    print(k_th_min(_arr, _k))
