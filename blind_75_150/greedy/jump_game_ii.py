from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        R -> O( max(nums) * len(nums) )
        S -> O(n)
        """
        if len(nums) == 1:
            return 0
        start = 0
        ans = 0
        while start < len(nums) - 1:
            furthest = 0
            step = 0
            if start + nums[start] >= len(nums) - 1:
                return ans + 1
            for i in range(1, nums[start] + 1):
                if i + nums[start + i] >= furthest:
                    furthest = i + nums[start + i]
                    step = i
            start += step
            ans += 1

        return ans

