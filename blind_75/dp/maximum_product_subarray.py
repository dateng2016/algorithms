from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # R -> O(n) this cannot be optimized since we have to traverse the
        #           entire array
        # S -> O(1) We are not using extra space

        ans = float("inf")
        # We keep a min
        # We keep a ans (overall_max)
        # We keep a cur_max
        prev_max = nums[0]
        prev_min = nums[0]
        ans = prev_max
        for i in range(len(nums)):
            # No matter what, we will ALWAYS include
            # the current number

            if i == 0:
                continue
            n = nums[i]
            cur_max = max(prev_max * n, n, prev_min * n)
            cur_min = min(prev_max * n, n, prev_min * n)
            ans = max(cur_max, ans)

            prev_max = cur_max
            prev_min = cur_min
        return ans

