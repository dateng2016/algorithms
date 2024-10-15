from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Optimization R: O(n)
        # We create a frequency list to avoid doing the sorting ourselves
        count = Counter(nums)  # O(n)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        pass

        # overall time: O(n*log(n)) Space: O(n)
        c = Counter(
            nums
        )  # Runtime O(n) where n is the length of nums. Space: O(n) assuming each element has one appearacne

        ls = list(c.keys())  # O(n)  O(n)
        ls.sort(key=lambda t: -c[t])  # O(n*log(n))
        res = []
        for i in range(k):
            res.append(ls[i])  # O(k)   note that k <= n
        return res

        # Therefore the
        pass

