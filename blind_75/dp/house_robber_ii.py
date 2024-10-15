from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_normal(nums: List[int]) -> int:
            # R -> O(n)
            # S -> O(n)
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]
            for i in range(1, len(nums)):
                dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
            return dp[-1]

        if len(nums) <= 3:
            return max(nums)
        # We can either rob the first one
        # OR NOT rob the first one
        return max(nums[0] + rob_normal(nums[2 : len(nums) - 1]), rob_normal(nums[1:]))

        # def rob_normal(nums):
        #     dp = [0] * (len(nums) + 1)
        #     dp[1] = nums[0]
        #     for i in range(1, len(nums)):
        #         dp[i + 1] = max(dp[i], dp[i-1] + nums[i])
        #     return dp[-1]
        # if len(nums) <= 3: return max(nums)
        # return max(rob_normal(nums[2:-1]) + nums[0], rob_normal(nums[1:]) )

