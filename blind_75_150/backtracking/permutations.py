from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        The provided function generates all permutations of a list of integers using depth-first search (DFS). Let's analyze the time complexity:

        Number of Permutations: For a list of length nn, the total number of permutations is n!n!. This is because each of the nn positions in the permutation can be filled in nn ways, n−1n−1 ways, down to 1 way, resulting in n!n! total arrangements.

        Constructing Each Permutation: Each permutation can take O(n)O(n) time to construct, as we are appending to the current permutation list (cur).

        Recursion Depth: The recursion goes to a depth of nn, since we need to build a permutation of length nn.

        Combining these points, the overall time complexity can be expressed as:
        O(n⋅n!)
        """
        res = []

        def dfs(cur: List[int], seen: Set[int]):
            if len(cur) == len(nums):
                res.append(cur)
                return
            for n in nums:
                if n not in seen:
                    new_seen = seen.copy()
                    new_seen.add(n)
                    dfs(cur + [n], new_seen)

        for n in nums:
            dfs([n], {n})
        return res

