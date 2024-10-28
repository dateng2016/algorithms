from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # * We keep track of number of LEFT and number of RIGHT we currently have
        # * If LEFT == RIGHT -> Next one has to be LEFT
        # * ELSE -> Next one can be LEFT if LEFT < n else Next one can be left or right
        # *
        # *
        res = []

        def dfs(cur, left, right):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if left == right:
                dfs(cur + "(", left + 1, right)
            else:
                if left < n:
                    dfs(cur + "(", left + 1, right)
                dfs(cur + ")", left, right + 1)

        dfs("(", 1, 0)
        return res


sol = Solution()
res = sol.generateParenthesis(3)
print(res)


s = "Generate Parentheses.py".lower()
ls = s.split(" ")
print("_".join(ls))

