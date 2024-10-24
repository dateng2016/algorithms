class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            remainder = n % 2
            if remainder == 1:
                ans += 1
            n //= 2
        return ans

