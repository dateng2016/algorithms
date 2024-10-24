class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # R -> O(r * c)
        # S -> O(r * c)
        r = len(text1)
        c = len(text2)
        dp = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                to_add = 1 if text1[i] == text2[j] else 0
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + to_add)
        return dp[-1][-1]

