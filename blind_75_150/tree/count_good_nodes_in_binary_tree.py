from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def helper(node: Optional[TreeNode], cur_max: int):
            if not node:
                return
            nonlocal ans
            if node.val >= cur_max:
                ans += 1
                cur_max = node.val
            helper(node.left, cur_max)
            helper(node.right, cur_max)

        helper(root, -float("inf"))
        return ans


s = "Count Good Nodes in Binary Tree.py".lower()
ls = s.split(" ")
print("_".join(ls))

