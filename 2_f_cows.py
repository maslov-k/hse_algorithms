def check_cows(coords, m, k):
    cows = 1
    last_coord = coords[0]

    for i in range(1, len(coords)):
        if coords[i] - last_coord >= m:
            cows += 1
            if cows >= k:
                return True
            last_coord = coords[i]

    return False


def stall_distance(coords, k):
    left = 0
    right = coords[-1]
    while left < right - 1:
        m = left + (right - left) // 2
        if check_cows(coords, m, k):
            left = m
        else:
            right = m

    return left


if __name__ == '__main__':
    _n, _k = map(int, input().split())
    _coords = list(map(int, input().split()))

    print(stall_distance(_coords, _k))
