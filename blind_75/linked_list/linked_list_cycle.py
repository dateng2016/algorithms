from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Use the Floyd's algorithm to make S -> O(1)   (NeetCode Guy)

        fast = head
        slow = head
        while fast and slow:
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if not fast:
                return False

            slow = slow.next

            if fast == slow:
                return True

        return "Hahahah"
        # Most intuitive way to do this is to use SET seen to
        # keep track what we have seen so far

        # We have R -> O(n)   this has to be because we need to traverse the entire thing
        # We have S -> O(n) we need to keep a hashset to keep track of what we have seen

        seen = set()

        cur = head

        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False


