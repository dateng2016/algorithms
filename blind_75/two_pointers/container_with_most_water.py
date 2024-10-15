from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # This solution has R -> O(n) and S -> O(1)
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            cur = min(height[l], height[r]) * (r - l)
            ans = max(cur, ans)

            move_left = True if height[l] <= height[r] else False
            move_right = True if height[r] <= height[l] else False
            # if the left side is the smaller one, then we move the left one
            # until we see a bigger one
            if move_left:
                target_left = height[l]
                while height[l] <= target_left and l < r:
                    l += 1
            if move_right:
                target_right = height[r]
                while height[r] <= target_right and l < r:
                    r -= 1

            # If the right side is the smaller one, we move the right one
            # until we see a bigger one

            # NOTE: If both are equal, then we move both until we see a bigger one
        return ans

