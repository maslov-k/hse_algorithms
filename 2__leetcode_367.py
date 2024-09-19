from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num // 2

        while left < right:
            m = left + (right - left) // 2

            if m * m < num:
                left = m + 1
            else:
                right = m

        return left * left == num


if __name__ == '__main__':
    solution = Solution()

    print(solution.isPerfectSquare(16))
