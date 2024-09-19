def single_value(nums):
    left = 0
    right = len(nums)

    if right == 1:
        return nums[0]

    while left < right - 3:
        m = left + (right - left) // 2 + 1
        m = m - 1 if nums[m - 1] == nums[m] else m
        if (m - left) % 2 == 0:
            left = m
        else:
            right = m

    return nums[left] if nums[left] != nums[left + 1] else nums[right - 1]


if __name__ == '__main__':
    _n = int(input())
    _nums = list(map(int, input().split()))

    print(single_value(_nums))
