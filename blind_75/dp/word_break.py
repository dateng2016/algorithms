from typing import List


class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        trie = Node()
        # We construct the Trie object

        # R -> O(word_length * dict_length)
        # S -> O(word_length * dict_length)

        for word in wordDict:
            cur = trie
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.is_end = True

        # Maxlength is dict_length
        next_to_check = [0]
        seen = set([0])

        def check(idx: int, cur: Node):
            # Here idx represents the next index that we need to check
            if cur.is_end:
                if idx not in seen:
                    seen.add(idx)
                    next_to_check.append(idx)
            if idx == len(s) or s[idx] not in cur.children:
                # Next character to check is not in the children
                return
            check(idx + 1, cur.children[s[idx]])

        # Now we check the string
        # R -> O(len(s) ** 2) since we might need to check for every
        #        character in the string till the end of it,
        #       We ensured that each index is only checked once
        # S -> O(1) We do not take extra space
        while next_to_check:
            idx = next_to_check.pop()
            if idx == len(s):
                return True
            check(idx, trie)
        return False

