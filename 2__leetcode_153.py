from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right - 1:
            _m = left + (right - left) // 2

            if nums[_m] > nums[left] and nums[_m] > nums[right]:
                left = _m
            else:
                right = _m

        return nums[right]


if __name__ == '__main__':
    solution = Solution()

    print(solution.findMin([6, 7, 0, 1, 2, 4, 5]))
    print(solution.findMin([3, 4, 5, 1, 2]))
    print(solution.findMin([11, 13, 15, 17]))
