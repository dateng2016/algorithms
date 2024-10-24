from typing import List


# def hammingWeight(n: int) -> int:
#     ans = 0
#     while n > 0:
#         remainder = n % 2
#         if remainder == 1:
#             ans += 1
#         n //= 2
#     return ans


from functools import lru_cache
from math import log2


class Solution:
    @lru_cache
    def countBits(self, n: int) -> List[int]:

        # if not n:
        #     return [0]
        # if n == 1:
        #     return [0, 1]
        # prev = self.countBits(n - 1)

        # idx = n - 2 ** int(log2(n))
        # if idx == 0:
        #     return prev + [1]
        # else:

        #     return prev + [prev[idx] + 1]
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[1] = 1
        off_set = 2
        for i in range(2, n + 1):
            off_set = 2 ** int(log2(i))
            dp[i] = dp[i - off_set] + 1
        return dp

