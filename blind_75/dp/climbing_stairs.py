from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Complexity: O(n)O(n) - because each unique state (step count) is computed only once due to memoization.
        # Space Complexity: O(n)O(n) - due to the memoization cache and the call stack.
        @lru_cache
        def helper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return helper(n - 1) + helper(n - 2)

        return helper(n)

