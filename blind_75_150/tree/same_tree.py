from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # R -> O(n) this has to be tree, because we need to traverse the
        #           entire tree for the worst case
        # S -> O(log n) for balanced tree. O(n) for the worst case due to the
        #           memory of the call stack

        def check(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        return check(p, q)

