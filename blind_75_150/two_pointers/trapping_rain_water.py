from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        # * NEETCODE GUY
        # * R -> O(n) S -> O(1)
        if len(heights) <= 1:
            return 0
        l, r = 0, len(heights) - 1
        left_max, right_max = heights[l], heights[r]
        ans = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, heights[l])
                ans += left_max - heights[l]
            else:
                r -= 1
                right_max = max(right_max, heights[r])
                ans += right_max - heights[r]
        return ans

        # * R -> O(n ** 2) for worst case, because we might need
        # * to traverse the entire stack every time
        # * S -> O(n) since the only thing that costs extra memory is the stack
        # * We can actually optimize this to be O(1) Since we do not actually need a stack

        if len(heights) <= 1:
            return 0
        stack = [heights[0]]  # * Keep track of the current_heights
        # We use a two pointer
        # i, j
        # Once heights[j] >= heights[i] we let i = j
        # Before that, we use a stack to keep the current_heights
        ans = 0
        i = 0
        j = 1
        while j < len(heights):
            if heights[j] >= heights[i]:
                # * Here we need to do some calculation
                highest_point = heights[i]
                for idx in range(1, len(stack)):
                    ans += highest_point - stack[idx]
                # * We need to move the first pointer to the second pointer
                i = j
                j += 1
                stack = [heights[i]]
            elif heights[j] <= heights[-1]:
                stack.append(heights[j])
                j += 1
            else:
                for idx in range(len(stack) - 1, -1, -1):
                    if stack[idx] < heights[j]:
                        ans += heights[j] - stack[idx]
                        stack[idx] = heights[j]
                    else:
                        break
                stack.append(heights[j])
                j += 1

        if stack:
            top = stack[-1]
            for h in stack:
                ans += max(top - h, 0)

        return ans


s = Solution()
s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

