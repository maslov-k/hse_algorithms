def window_min(nums, k):
    result = []

    stack_in = []
    stack_out = []

    stack_in_min = nums[0]

    for i in range(k):
        stack_in.append(nums[i])
        stack_in_min = min(stack_in_min, nums[i])

    result.append(stack_in_min)

    for i in range(k, len(nums)):
        if not stack_out:
            while stack_in:
                val = stack_in.pop()
                stack_out.append(val if not stack_out else min(stack_out[-1], val))

        new_val = nums[i]

        stack_out.pop()
        stack_in_min = new_val if not stack_in else min(stack_in_min, new_val)
        stack_in.append(new_val)

        result.append(stack_in_min if not stack_out else min(stack_out[-1], stack_in_min))

    return result


if __name__ == '__main__':
    _n, _k = map(int, input().split())
    _nums = list(map(int, input().split()))

    for n in window_min(_nums, _k):
        print(n)
