def medians(arrays):
    result = []
    merger_size = len(arrays[0]) * 2

    for i in range(len(arrays)):
        for j in range(i + 1, len(arrays)):
            arr_1 = arrays[i]
            arr_2 = arrays[j]

            mid = merger_size // 2 - 1

            k_1 = 0
            k_2 = 0

            while k_1 + k_2 < mid:
                if arr_1[k_1] < arr_2[k_2]:
                    k_1 += 1
                else:
                    k_2 += 1

            mid_el_1 = min(arr_1[k_1], arr_2[k_2])

            if arr_1[k_1] < arr_2[k_2]:
                k_1 += 1
            else:
                k_2 += 1

            mid_el_2 = min(arr_1[k_1], arr_2[k_2])

            result.append(mid_el_2 if merger_size % 2 != 0 else (mid_el_1 + mid_el_2) / 2)

    return result


if __name__ == '__main__':
    _n, _m = map(int, input().split())

    _arrays = []

    for _ in range(_n):
        arr = list(map(int, input().split()))

        _arrays.append(arr)

    _medians = medians(_arrays)

    for m in _medians:
        print(f'{m:.5f}')
