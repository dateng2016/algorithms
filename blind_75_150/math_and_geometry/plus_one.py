from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        idx = len(digits) - 1
        while carry and idx >= 0:
            result = digits[idx] + 1
            if result < 10:
                digits[idx] = result
                carry = 0
                break
            digits[idx] = 0
            idx -= 1
        print(carry, idx)
        return digits if not carry else [1] + digits


sol = Solution()
res = sol.plusOne([1, 2, 3])
print(res)