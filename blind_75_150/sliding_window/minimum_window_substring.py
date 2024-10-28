from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # * R -> O(n)
        # * S -> O(n)
        if len(t) == 1:
            return t if t in s else ""
        # * First we initialize i = j = 0, t_count = Counter(t)
        i = j = 0
        t_count = Counter(t)
        target_num_conditions = len(t_count)
        num_conditions_met = 0
        s_count = defaultdict(int)
        ans_len = float("inf")
        ans = ""
        # * We keep doing j++ operation until s_count[key] >= t_count[key] for all keys in t_count
        while j < len(s):
            character = s[j]
            s_count[character] += 1
            if (
                s_count[character] == t_count[character]
            ):  # * This means that we are having ONE MORE condition met
                num_conditions_met += 1
                # * We use a variable "num_conditions_met" to keep track of the number of keys that satisfy the above condition
                # * When "num_conditions_met == len(set(t))", we have found ONE substring
                if num_conditions_met == target_num_conditions:
                    # * To ensure this substring is minimum, we doing the i++ operation until num_conditions_met < len(set(t))
                    while num_conditions_met == target_num_conditions:
                        starting_char = s[i]
                        s_count[starting_char] -= 1
                        if (
                            starting_char in t_count
                            and s_count[starting_char] < t_count[starting_char]
                        ):
                            num_conditions_met -= 1
                        i += 1
                    # * At this time, [i-1, j] is the minimum string that we are looking for
                    if ans_len > j - (i - 1) + 1:
                        ans = s[i - 1 : j + 1]
                        ans_len = j - (i - 1) + 1
                    # * After this, we continue to do the j++ and so on...
            j += 1

        return ans

