from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # * R -> O(3 ** n)
        # * S -> O(3 ** n)

        if not digits:
            return []
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(idx, cur: str):
            # * NOTE: idx has NOT been used yet
            if idx == len(digits):
                res.append(cur)
                return
            d = digits[idx]
            for ch in digit_to_letters[d]:
                dfs(idx + 1, cur + ch)

        dfs(0, "")
        return res

