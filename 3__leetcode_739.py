from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                cold_i = stack[-1]
                result[cold_i] = i - cold_i
                stack.pop()

            stack.append(i)

        return result


if __name__ == '__main__':
    solution = Solution()

    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
