from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def helper(node: TreeNode, min_val: int, max_val: int):
            nonlocal ans
            if not ans:
                # If we found a place that is wrong, we don't
                # do any further check. (Early Stop)
                return
            if not node.left and not node.right:
                return
            if node.left and (node.left.val >= node.val or node.left.val <= min_val):
                ans = False
                return
            if node.right and (node.right.val <= node.val or node.right.val >= max_val):
                ans = False
                return
            if node.left:
                # Update its max_val
                helper(node.left, min_val, node.val)
            if node.right:
                # Update its min_val
                helper(node.right, node.val, max_val)

        helper(root, -float("inf"), float("inf"))
        return ans

