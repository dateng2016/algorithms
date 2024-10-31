from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # * Better Approach (Inspiration from NEETCODE GUY)
        if len(heights) == 1:
            return heights[0]
        ans = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack:
                stack.append((i, h))
                continue
            prev_idx = None
            while stack and stack[-1][1] > h:
                prev_idx, prev_height = stack.pop()
                ans = max(ans, (i - prev_idx) * prev_height)
            if prev_idx is None:
                stack.append((i, h))
            else:
                stack.append((prev_idx, h))
        end = len(heights)
        while stack:
            prev_idx, prev_height = stack.pop()
            ans = max(ans, (end - prev_idx) * prev_height)
        return ans

        # *********************************************8
        if len(heights) == 1:
            return heights[0]
        ans = 0
        stack = []
        rec_left = [0] * len(heights)
        rec_right = [0] * len(heights)
        for i, h in enumerate(heights):
            # print(stack)
            if not stack:
                stack.append((i, h))
                continue
            while stack and stack[-1][1] > h:
                prev_idx, prev_height = stack.pop()
                # ans = max(ans, (i - prev_idx) * prev_height)
                rec_right[prev_idx] = (i - prev_idx) * prev_height
            stack.append((i, h))
            # print(stack)
            # print()
        end = len(heights)
        while stack:
            prev_idx, prev_height = stack.pop()
            # ans = max(ans, (end - prev_idx) * prev_height)
            rec_right[prev_idx] = (end - prev_idx) * prev_height

        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]
            # print(stack)
            if not stack:
                stack.append((i, h))
                continue
            while stack and stack[-1][1] > h:
                post_idx, post_height = stack.pop()
                # ans = max(ans, (post_idx - i) * post_height)
                rec_left[post_idx] = (post_idx - i) * post_height
            stack.append((i, h))
            # print(stack)
            # print()
        start = -1
        while stack:
            post_idx, post_height = stack.pop()
            # ans = max(ans, (post_idx - start) * post_height)
            rec_left[post_idx] = (post_idx - start) * post_height

        for i in range(len(heights)):
            ans = max(
                ans,
                rec_left[i] + rec_right[i] - heights[i],
                # , rec_left[i], rec_right[i]
            )
        # print(rec_left, rec_right)
        return ans


sol = Solution()
heights = [2, 1, 2]
sol.largestRectangleArea(heights)


s = "Largest Rectangle in Histogram.py".lower()
ls = s.split(" ")
print("_".join(ls))

