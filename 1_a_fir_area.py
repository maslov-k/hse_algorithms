def fir_area(branches_count):
    branches_area = (branches_count + 1) * branches_count
    trunk_area = branches_count * 2 + 1

    return branches_area + trunk_area


def test():
    assert fir_area(0) == 1
    assert fir_area(1) == 5
    assert fir_area(2) == 11
    assert fir_area(3) == 19


if __name__ == '__main__':
    n = int(input())
    print(fir_area(n))
