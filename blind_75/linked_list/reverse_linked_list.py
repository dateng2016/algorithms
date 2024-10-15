from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We know that we have to traverse the entire thing,
        # Therefore, the minimum for R is O(n)

        # Let's try to do it in a recursive way
        if not head:
            return head

        new_head = None

        def helper(prev: Optional[ListNode], cur: Optional[ListNode]) -> ListNode:
            if not cur.next:
                cur.next = prev
                nonlocal new_head
                new_head = cur
                return cur
            nxt = helper(cur, cur.next)
            cur.next = prev
            nxt.next = cur
            return cur

        helper(None, head)

        return new_head

        # We can get rid of the list that we use to keep track
        # for the ListNode

        if not head:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return

        # Brute force, we put all the nodes into a list,
        # and reverse the order from there
        # R -> O(n)  S -> O(n)
        if not head:
            return head
        cur = head
        ls: List[ListNode] = []
        while cur:
            ls.append(cur)
            cur = cur.next
        for i in range(len(ls) - 1, 0, -1):
            ls[i].next = ls[i - 1]
        ls[0].next = None
        return ls[-1]



