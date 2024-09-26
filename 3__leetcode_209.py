from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        n = len(nums)
        ans = n + 1
        for right in range(n):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    solution = Solution()

    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

