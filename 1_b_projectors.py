def projectors_time(proj_l, proj_m, proj_r):
    proj_l_limit = 4 * proj_l
    proj_m_limit = 2 * proj_m + 1
    proj_p_limit = 4 * proj_r + 2

    return min(proj_l_limit, proj_p_limit, proj_m_limit)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    print(projectors_time(a, b, c))
