from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Go through the entire list, sort each string
        # Use the count of charactors as keys to map it to the anagram list
        # Time complexity of O(nm) where n is the length of the list,
        #                       m is the length of each string

        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord("a")
                count[idx] += 1
            res[tuple(count)].append(s)
        return res.values()

        pass
        res = []
        d = dict()
        for s in strs:  # O(n) where n is the length of the strs list
            sorted_str = "".join(
                sorted(s)
            )  # O(m log(m)) where m is the length of the string, we can probably ignore
            if sorted_str in d:  # O(1)
                res[d[sorted_str]].append(s)
            else:
                d[sorted_str] = len(res)
                res.append([s])
        return res

        pass
        # Brute force
        # Time: O(n**2)
        # Space O(n)
        counter_ls = []
        res = []
        for s in strs:  # O(n)
            c = Counter(s)  # O(m) where m is the length of the string
            if c in counter_ls:
                idx = counter_ls.index(c)
                res[idx].append(s)
            else:
                counter_ls.append(c)
                res.append([s])
        return res

        # We need to optimize time

