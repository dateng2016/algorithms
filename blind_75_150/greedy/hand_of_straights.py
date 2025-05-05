from typing import List
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        R -> O(N log(N)) need to account for sorting
        S -> O(N log(N)) need to account for sorting
        """
        l = len(hand)
        if groupSize == 1:
            return True
        if l % groupSize != 0:
            return False
        frequency = Counter(hand)
        keys = list(frequency.keys())
        keys.sort()  # * O(N log (N))
        start_idx = 0

        while start_idx < len(keys):
            start_num = keys[start_idx]
            arr = [start_num]
            frequency[start_num] -= 1
            cur = start_num + 1
            while len(arr) < groupSize:
                if cur not in frequency or frequency[cur] == 0:
                    return False
                frequency[cur] -= 1
                arr.append(
                    cur
                )  # * This can be optimized a little bit, We do not need to keep a separate array
                # * Just the length is good enough
                cur += 1
            while start_idx < len(keys) and frequency[keys[start_idx]] == 0:
                start_idx += 1
            # print(
            #     arr,
            #     frequency,
            # )
        return True


s = Solution()
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
res = s.isNStraightHand(hand, groupSize)
print(res)

