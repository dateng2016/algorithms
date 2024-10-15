from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # R -> O(n)
        # S -> O(n)

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
        return dp[-1]


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         dp = [0] * (len(nums) + 1)
#         dp[1] = nums[0]
#         for i in range(1, len(nums)):
#             dp[i + 1] = max(dp[i], dp[i-1] + nums[i])
#         return dp[-1]

