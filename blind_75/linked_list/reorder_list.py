from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # NeetCode Guy: split the chain in half (using the fast & slow pointers)
        # Reverse the second half. Then do the merge
        # S -> O(1)

        # Do the split
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None

        # Reverse the second half
        cur: ListNode = second_head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second_head = prev
        first_head = head

        cur1 = first_head
        cur2 = second_head

        prev = None
        while cur1 and cur2:
            if prev:
                prev.next = cur1
            cur1_next = cur1.next
            cur1.next = cur2
            prev = cur2
            cur1 = cur1_next
            cur2 = cur2.next
        if cur1 and prev:
            prev.next = cur1

        return

        # We put everything into a list and then use a two pointer
        # R -> O(n) S -> O(n)
        if not head or not head.next:
            return
        cur = head
        ls: List[ListNode] = []
        while cur:
            ls.append(cur)
            cur = cur.next
        i = 0
        j = len(ls) - 1
        prev = None
        while i < j:
            ls[i].next = ls[j]
            if prev:
                prev.next = ls[i]
            prev = ls[j]
            i += 1
            j -= 1
        if i == j:
            prev.next = ls[i]
        ls[i].next = None


s = "Reorder List.py".lower()
ls = s.split(" ")
print("_".join(ls))


# from typing import Optional, List


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# def construct_list_nodes(arr: List) -> ListNode:
#     head = ListNode(arr[0])

#     cur = head
#     i = 1
#     while i < len(arr):
#         cur.next = ListNode(arr[i])
#         cur = cur.next
#         i += 1
#     return head


# def output_list_from_node(head: ListNode) -> List:
#     arr = []
#     cur = head
#     while cur:
#         arr.append(cur.val)
#         cur = cur.next
#     print(arr)


# arr = [1, 2, 3, 4, 5]
# head = construct_list_nodes(arr)
# output_list_from_node(head)


# def reverse(head: ListNode):
#     prev = None
#     cur = head
#     while cur:
#         nxt = cur.next
#         cur.next = prev
#         prev = cur
#         cur = nxt
#     return prev


# reversed_head = reverse(head)
# output_list_from_node(reversed_head)

