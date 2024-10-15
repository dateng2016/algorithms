from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # In order traversal
        # Left Root Right

        # For the worst case the R -> AT LEAST O(n), if it is completed unbalanced

        count = 0
        ans = None

        def in_order(node: TreeNode):
            nonlocal count
            nonlocal ans
            if count >= k:
                return
            if not node:
                return
            in_order(node.left)
            count += 1
            if count == k:
                ans = node.val
            in_order(node.right)

        in_order(root)
        return ans

