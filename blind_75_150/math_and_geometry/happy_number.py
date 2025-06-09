class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {n}
        if n == 1:
            return True

        def helper(n: int):
            n_str = str(n)
            total = 0
            for digit in n_str:
                total += int(digit) ** 2
            return int(total)

        while True:
            n = helper(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
