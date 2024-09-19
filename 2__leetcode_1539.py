from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss_cnt = 0
        prev_num = 0

        for n in arr:
            new_miss_cnt = miss_cnt + n - prev_num - 1
            if new_miss_cnt >= k:
                return prev_num + k - miss_cnt
            miss_cnt = new_miss_cnt
            prev_num = n

        return prev_num + k - miss_cnt


if __name__ == '__main__':
    solution = Solution()
    result = solution.findKthPositive([4, 5, 6], 4)

    print(result)
