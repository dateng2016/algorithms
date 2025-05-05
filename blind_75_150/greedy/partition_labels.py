from typing import List
from collections import Counter


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        R -> O(n)
        S -> O(26)
        """
        if len(s) == 1:
            return [1]
        frequency = Counter(s)
        res = []
        i = 0
        cur_length = 0
        to_eliminate = set()
        while i < len(s):
            char = s[i]
            cur_length += 1
            to_eliminate.add(char)
            frequency[char] -= 1
            if frequency[char] == 0:
                to_eliminate.remove(char)
            if not to_eliminate:
                res.append(cur_length)
                cur_length = 0
            i += 1
        return res


sol = Solution()
s = "ababcbacadefegdehijhklij"
res = sol.partitionLabels(s)
print(res)

