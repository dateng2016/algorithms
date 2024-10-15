class Solution:
    def countSubstrings(self, s: str) -> int:
        # This is the same as the previous one
        count = len(s)

        def expand(l, r):
            nonlocal count
            while 0 <= l and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(len(s) - 1):
            expand(i, i)
            expand(i, i + 1)
            count -= 1
        return count

