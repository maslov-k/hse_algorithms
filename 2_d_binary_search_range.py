def binary_search_left(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        m = left + (right - left) // 2

        if arr[m] < x:
            left = m + 1
        else:
            right = m

    return left


def binary_search_right(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        m = left + (right - left) // 2

        if arr[m] <= x:
            left = m + 1
        else:
            right = m

    return left


def binary_search_range(arr, x):
    first_entry = binary_search_left(arr, x)

    if first_entry < len(arr) and arr[first_entry] == x:
        second_entry = binary_search_right(arr, x)
        return first_entry + 1, second_entry

    return [0]


if __name__ == '__main__':
    _n, _m = map(int, input().split())

    _nums = list(map(int, input().split()))
    _xs = list(map(int, input().split()))

    for _x in _xs:
        print(*binary_search_range(_nums, _x))
