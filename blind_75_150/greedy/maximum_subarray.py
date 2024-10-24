from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        # R -> O(n)
        # S -> O(1)
        cur_sum = 0

        for n in nums:
            cur_sum += n
            if cur_sum < 0:
                cur_sum = 0

            ans = max(ans, cur_sum)
        return ans if ans > 0 else max(nums)

        # cur_max = 0
        # overall_max = -float('inf')
        # for n in nums:
        #     cur_max = max(n, n + cur_max)
        #     overall_max = max(cur_max, overall_max)
        # return overall_max

