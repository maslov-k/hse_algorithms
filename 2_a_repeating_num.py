def repeating_num(nums):
    tortoise = nums[0]
    hare = nums[nums[0]]

    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]

    tortoise = 0
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return tortoise


if __name__ == '__main__':
    _nums = list(map(int, input().split()))

    print(repeating_num(_nums))
