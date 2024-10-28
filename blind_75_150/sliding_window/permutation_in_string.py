from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # * R -> O(26n)
        # * S -> O(26) or O(1)

        if len(s2) < len(s1):
            return False

        s1_count = Counter(s1)
        for i in range(len(s1)):
            c = s2[i]
            if c in s1_count:
                s1_count[c] -= 1
        # found = True
        # for c in s1_count:
        #     if s1_count[c]:
        #         found = False
        #         break
        # if found:
        #     return found

        l = 0
        r = len(s1) - 1

        while r < len(s2):
            found = True
            for c in s1_count:  # * This will go 26 iterations at MAX
                if s1_count[c]:
                    found = False
                    break
            if found:
                return found

            left_char = s2[l]
            if left_char in s1_count:
                s1_count[left_char] += 1
            l += 1
            r += 1
            if r < len(s2) and s2[r] in s1_count:
                s1_count[s2[r]] -= 1
        return False

