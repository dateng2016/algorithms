class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP Method

        # Expand Mehod
        # R -> O(n ** 2)
        # S -> O(n) account for call stack
        # S -> O(1) by eliminating the call stack

        if len(s) <= 1:
            return s

        # def expand(l, r):
        #     # We have reached the end
        #     if l == 0 or r == len(s) - 1:
        #         return s[l : r + 1]
        #     if s[l - 1] == s[r + 1]:
        #         return expand(l - 1, r + 1)
        #     return s[l : r + 1]

        # We can optimize the expand function
        def expand(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        ans = ""
        for i in range(len(s) - 1):
            odd_expand = expand(i, i)
            even_expand = expand(i, i + 1)
            if len(odd_expand) > len(ans):
                ans = odd_expand
            if len(even_expand) > len(ans):
                ans = even_expand
        return ans

