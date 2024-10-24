class Solution:
    def numDecodings(self, s: str) -> int:
        # R -> O(n)
        # S -> O(n)

        # d = {str(i): chr(ord("A") + i - 1) for i in range(1, 27)}

        # Can be combined with the previous
        # HAVE to be combined
        # Cannot be combined

        dp = (len(s) + 1) * [0]
        dp[0] = 1
        for i in range(len(s)):
            # We work on dp[i + 1]
            if i == 0:
                if s[i] == "0":
                    return 0
                dp[i + 1] = 1

            # From this point on i >= 1
            elif s[i] == "0":
                if s[i - 1] != "1" and s[i - 1] != "2":
                    return 0
                dp[i + 1] = dp[i - 1]
            elif 11 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                # Cannot be combined
                dp[i + 1] = dp[i]
        return dp[-1]


# This is my solution before

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         if s[0] == '0':
#             return 0
#         dp = [0 for _ in range(len(s) + 1)]
#         dp[1] = 1
#         dp[0] = 1
#         flexible = [False for _ in range(len(s) + 1)]
#         for i in range(1, len(s)):
#             if s[i] != '0':
#                 # It serves as a single digit
#                 dp[i+1] += dp[i]
#             if '10' <= s[i-1:i+1] <= '26':
#                 dp[i+1] += dp[i-1]
#         return dp[-1]

