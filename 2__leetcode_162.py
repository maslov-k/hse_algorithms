from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            m = left + (right - left) // 2

            if nums[m - 1] < nums[m] < nums[m + 1]:
                left = m
            else:
                right = m

        return left if nums[left] > nums[right] else right


if __name__ == '__main__':
    solution = Solution()

    print(solution.findPeakElement([1, 2, 3, 5, 6, 7, 8, 9, 8, 7]))
    print(solution.findPeakElement([1, 2, 3, 1]))
    print(solution.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
    print(solution.findPeakElement([2, 1]))
    print(solution.findPeakElement([6, 5, 4, 3, 2, 3, 2]))
