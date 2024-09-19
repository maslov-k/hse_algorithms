def start_index(nums):
    _left = 0
    _right = len(nums) - 1

    if nums[_left] < nums[_right]:
        return _left

    while _left < _right - 1:
        _m = _left + (_right - _left) // 2

        if nums[_m] > nums[_left] and nums[_m] > nums[_right]:
            _left = _m
        else:
            _right = _m

    return _right


def search(nums, x):
    start_ind = start_index(nums)
    left = start_ind - len(nums) if start_ind > 0 else start_ind
    right = len(nums) + left

    while left < right - 1:
        m = left + (right - left) // 2

        if nums[m] <= x:
            left = m
        else:
            right = m

    index = left if left >= 0 else left + len(nums)

    return index if nums[index] == x else -1


if __name__ == '__main__':
    _n = int(input())
    _nums = list(map(int, input().split()))
    _x = int(input())

    print(search(_nums, _x))
