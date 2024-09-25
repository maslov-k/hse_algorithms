from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        sub_sum = 0

        for n in nums:
            if sub_sum < 0:
                sub_sum = 0

            sub_sum += n

            result = max(result, sub_sum)

        return result


class SolutionDC:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, suf = [*nums], [*nums]
        for i in range(1, len(nums)):       pre[i] += max(0, pre[i - 1])
        for i in range(len(nums) - 2, -1, -1):  suf[i] += max(0, suf[i + 1])

        def maxSubArray(a, left, right):
            if left == right:
                return a[left]

            mid = (left + right) // 2

            return max(maxSubArray(a, left, mid), maxSubArray(a, mid + 1, right), pre[mid] + suf[mid + 1])

        return maxSubArray(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    solution = Solution()
    solutionDc = SolutionDC()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solutionDc.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



