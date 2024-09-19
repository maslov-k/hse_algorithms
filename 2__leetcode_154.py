from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] == nums[right]:
            new_right = 0
            while nums[new_right] == nums[-1]:
                new_right += 1
                if new_right == len(nums):
                    return nums[0]

            right = new_right - 1
            left = right - len(nums) + 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right - 1:
            _m = left + (right - left) // 2

            if nums[_m] >= nums[left] and nums[_m] >= nums[right]:
                left = _m
            else:
                right = _m

        return nums[right]


if __name__ == '__main__':
    solution = Solution()

    print(solution.findMin([2, 2, 2, 0, 1]))
    print(solution.findMin([1, 3, 5]))
    print(solution.findMin([6, 7, 7, 0, 0, 1, 2, 2, 4, 5]))
    print(solution.findMin([3, 3, 4, 5, 1, 2, 2]))
    print(solution.findMin([11, 13, 13, 13, 15, 17, 17]))
    print(solution.findMin([10, 10, 10, 10]))
