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


if __name__ == '__main__':
    solution = Solution()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



