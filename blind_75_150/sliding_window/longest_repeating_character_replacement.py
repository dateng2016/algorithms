from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # R -> O(n), S -> O(1), We are assuming the max(count.values()) has a
        # runtime of O(n) since it can only contain max of 26 keys and values pairs
        if k >= len(s):
            return len(s)
        i = 0
        j = k
        count = Counter(s[i : k + 1])
        max_count = max(count.values())
        ans = 1
        while j < len(s):
            # if the total length of the current string
            # MINUS
            # the max_count
            # IS GREATER THAN
            # k
            # Then we need to move the left pointer until the following condition is met
            # total_length - max_count <= k
            total_length = j - i + 1
            while total_length - max_count > k:
                count[s[i]] -= 1
                i += 1
                total_length -= 1
                max_count = max(count.values())
            ans = max(ans, total_length)
            # print(i, j, total_length, ans)

            j += 1
            if j < len(s):
                count[s[j]] += 1
                max_count = max(count[s[j]], max_count)
        return ans


