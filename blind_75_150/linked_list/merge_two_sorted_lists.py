from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # We use two pointer to keep track of the two lists
        # We append the smaller one to the next one in the queue
        # R -> O(n) S -> O(1)
        if not list1:
            return list2
        if not list2:
            return list1

        cur1 = list1
        cur2 = list2

        cur = None
        head = None

        if cur1.val < cur2.val:
            cur = cur1
            head = cur
            cur1 = cur1.next
        else:
            cur = cur2
            head = cur
            cur2 = cur2.next

        while cur1 and cur2:
            # Do the comparision
            if cur1.val < cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        if cur1:
            cur.next = cur1
        elif cur2:
            cur.next = cur2
        return head


