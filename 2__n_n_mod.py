def n_n_mod(n, m):
    n_mod_m = n % m

    result = 1

    for i in range(n):
        result *= n_mod_m
        result %= m

    return result


if __name__ == '__main__':
    _n, _m = map(int, input().split())

    print(n_n_mod(_n, _m))
