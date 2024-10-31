from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, head1: Optional[ListNode], head2: Optional[ListNode]
    ) -> Optional[ListNode]:
        exponent1 = exponent2 = 0
        cur1 = head1
        num1 = 0
        while cur1:
            num1 += cur1.val * 10**exponent1
            exponent1 += 1
            cur1 = cur1.next
        cur2 = head2
        num2 = 0
        while cur2:
            num2 += cur2.val * 10**exponent2
            exponent2 += 1
            cur2 = cur2.next
        total = num1 + num2
        new_head = None
        cur = None

        # Build the linked list from the total
        for digit in str(total)[::-1]:  # Reverse the string representation of the total
            new_node = ListNode(int(digit))
            if not new_head:
                new_head = new_node
                cur = new_head
            else:
                cur.next = new_node
                cur = cur.next

        return new_head


s = "Add Two Numbers.py".lower()
ls = s.split(" ")
print("_".join(ls))

