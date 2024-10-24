from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # We traverse the entire array and do a binary search
        # On the subsequence array that keep track
        # R -> O(n log n)
        # S -> O(n)
        subsequence = []
        for n in nums:
            if not subsequence or subsequence[-1] < n:
                subsequence.append(n)
            else:
                idx = bisect_left(
                    subsequence, n
                )  # Find the index of the first element >= n
                subsequence[idx] = n  # Replace that number with n
        return len(subsequence)

        # R -> O(2 ** n)

        # DFS Solution
        seen = set()
        # cur_max = -float("inf")
        ans = 1

        def dfs(idx, length):
            ans = length
            seen.add(idx)
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    ans = max(ans, dfs(i, length + 1))
            return ans

        for i in range(len(nums)):

            if i not in seen:
                ans = max(ans, dfs(i, 1))

        return ans

        # R -> O(n ** 2)
        # S -> O(n)
        d = defaultdict(int)
        for n in nums:
            d[n] = 1
            for key in d:
                if key < n:
                    d[n] = max(d[n], d[key] + 1)
        return max(d.values())

