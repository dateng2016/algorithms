from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        R -> O(n)
        S -> O(1)
        """
        seen = set()
        t_a, t_b, t_c = target
        for a, b, c in triplets:
            if a > t_a or b > t_b or c > t_c:
                continue
            if a == t_a and b == t_b and c == t_c:
                return True
            if a == t_a:
                if ("b", "c") in seen or ("b" in seen and "c" in seen):
                    return True
                seen.add("a")
            if b == t_b:
                if ("a", "c") in seen or ("a" in seen and "c" in seen):
                    return True
                seen.add("b")
            if c == t_c:
                if ("a", "b") in seen or ("a" in seen and "b" in seen):
                    return True
                seen.add("c")
            if a == t_a and b == t_b:
                if "c" in seen:
                    return True
                seen.add(("a", "b"))
            if a == t_a and c == t_c:
                if "b" in seen:
                    return True
                seen.add(("a", "c"))
            if c == t_c and b == t_b:
                if "a" in seen:
                    return True
                seen.add(("b", "c"))

        return False


s = Solution()
triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
target = [5, 5, 5]
res = s.mergeTriplets(triplets=triplets, target=target)
print(res)

