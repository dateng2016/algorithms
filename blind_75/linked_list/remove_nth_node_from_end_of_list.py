from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # NeetCode Guy: He can do it in ONE pass
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            right = right.next
            n -= 1
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

        return dummy.next

        # First approach is that we use a list
        # This will give R -> O(n) and S -> O(n)
        # We can optimize the S -> O(1)
        idx = 0
        cur = head
        while cur:
            cur = cur.next
            idx += 1
        # idx starts as 0
        # final idx - 1 corresponds to the end node
        final_idx = idx - 1
        target_idx = final_idx + 1 - n
        cur = head
        idx = 0
        prev = None
        while cur:
            if idx == target_idx:
                if not prev:
                    return cur.next
                else:
                    prev.next = cur.next
                    return head
            prev = cur
            cur = cur.next
            idx += 1

