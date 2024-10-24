import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # R -> O(amount * len(coins))
        # S -> O(amount)

        coins.sort()
        dp = [0] + [float("inf")] * amount
        for coin in coins:
            if coin > amount:
                continue
            # Update dp starting i
            for i in range(1, len(dp)):
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] < float("inf") else -1

        # This is my previous solution
        # dp = [math.inf] * (amount + 1)
        # dp[0] = 0

        # for coin in coins:
        #     for i in range(coin, amount + 1):
        #         dp[i] = min(dp[i], dp[i - coin] + 1)

        # return -1 if dp[-1] == math.inf else dp[-1]


s = Solution()
ans = s.coinChange([1, 2, 5], 11)

