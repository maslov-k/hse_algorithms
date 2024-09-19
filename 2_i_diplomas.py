def board_area(w, h, n):
    left = max(w, h)
    right = left * n

    while left < right:
        m = left + (right - left) // 2
        if (m // h) * (m // w) < n:
            left = m + 1
        else:
            right = m

    return left


if __name__ == '__main__':
    _w, _h, _n = map(int, input().split())

    print(board_area(_w, _h, _n))
