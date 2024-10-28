class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Here we use a sliding window to solve this problem
        # R -> O(n) S -> O(1)
        if len(s) <= 1:
            return len(s)
        ans = 1

        l = 0
        r = 1
        seen = set()
        seen.add(s[l])
        while r < len(s):
            if s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                if l < r:
                    l += 1
            seen.add(s[r])
            ans = max(ans, r - l + 1)
            r += 1
            print(seen)
        return ans

