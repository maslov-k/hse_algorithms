def max_subarray_sum(nums):
    result = nums[0]
    current_sum = 0

    temp_left = 0
    left = 0
    right = 0

    for i in range(len(nums)):
        if current_sum <= 0:
            current_sum = 0
            temp_left = i

        current_sum += nums[i]

        if current_sum > result:
            result = current_sum
            right = i
            left = temp_left

    return [left, right]


if __name__ == '__main__':
    _n = int(input())
    _nums = list(map(int, input().split()))

    print(*max_subarray_sum(_nums))
