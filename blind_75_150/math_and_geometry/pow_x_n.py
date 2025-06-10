class Solution:
    def myPow(self, x: float, n: int) -> float:
        # * Optimized by GPT
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2
        return ans

        # * My Solution
        ans = x
        d = {0: 1, 1: x}
        max_exp = 1
        while max_exp <= abs(n):
            d[max_exp * 2] = d[max_exp] * d[max_exp]
            max_exp *= 2

        keys = []
        target = abs(n)
        cur_exp = max_exp
        # ans = 1
        while target:
            if cur_exp > target:
                cur_exp //= 2
                continue
            keys.append(cur_exp)
            target -= cur_exp
        ans = 1
        for key in keys:
            ans *= d[key]
        return ans if n > 0 else 1 / ans


sol = Solution()
res = sol.myPow(2, -200000000)
print(res)
