from typing import List


class Solution:
    def start_index(self, nums: List[int]) -> int:
        _left = 0
        _right = len(nums) - 1

        if nums[_left] < nums[_right]:
            return _left

        while _left < _right - 1:
            _m = _left + (_right - _left) // 2

            if nums[_m] > nums[_left] and nums[_m] > nums[_right]:
                _left = _m
            else:
                _right = _m

        return _right

    def search(self, nums: List[int], target: int) -> int:
        start_index = self.start_index(nums)
        left = start_index - len(nums) if start_index > 0 else start_index
        right = len(nums) + left

        while left < right - 1:
            m = left + (right - left) // 2

            if nums[m] <= target:
                left = m
            else:
                right = m

        index = left if left >= 0 else left + len(nums)

        return index if nums[index] == target else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([1, 3], 3))
    print(solution.search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7))
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))

    # print(result)
