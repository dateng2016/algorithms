class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        R -> O(n)
        S -> O(n)
        """
        star_count = 0
        left_count = 0
        right_count = 0
        # * Forward Traversal -> Make sure that we can cover all the ')'
        for ch in s:
            if ch == "(":
                left_count += 1
            elif ch == ")":
                right_count += 1
            elif ch == "*":
                star_count += 1
            if right_count > left_count:
                if star_count == 0:
                    return False
                star_count -= 1
                left_count += 1
        # * Backward Traversal -> Make sure we can cover all the '('
        star_count = 0
        left_count = 0
        right_count = 0
        for ch in s[::-1]:
            if ch == "(":
                left_count += 1
            elif ch == ")":
                right_count += 1
            elif ch == "*":
                star_count += 1
            if left_count > right_count:
                if star_count == 0:
                    return False
                star_count -= 1
                right_count += 1
        return True

