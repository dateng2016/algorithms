from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # * R -> O(n)
        # * S -> O(n)
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            while stack and stack[-1][0] < cur_temp:
                prev_temp, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((cur_temp, i))
        return res


s = "Daily Temperatures.py".lower()
ls = s.split(" ")
print("_".join(ls))

