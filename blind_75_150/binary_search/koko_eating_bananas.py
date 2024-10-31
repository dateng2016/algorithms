from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = float("inf")
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += p // mid if p % mid == 0 else p // mid + 1
            if hours <= h:
                ans = min(ans, mid)
                # * We want the answer to be even smaller if possible
                right = mid - 1
            else:
                left = mid + 1
        return ans


s = "Koko Eating Bananas.py".lower()
ls = s.split(" ")
print("_".join(ls))

