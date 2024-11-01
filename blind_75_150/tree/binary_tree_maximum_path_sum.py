from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float("inf")

        def helper(node: Optional[TreeNode]):
            if not node:
                return None
            nonlocal ans
            max_left = helper(node.left)
            max_right = helper(node.right)
            if not max_left and not max_right:
                ans = max(ans, node.val)
                return node.val
            elif not max_left:
                # * We only have max_right
                ans = max(ans, node.val, max_right + node.val)
                return max(node.val, node.val + max_right)
            elif not max_right:
                # * We only have max_left
                ans = max(ans, node.val, max_left + node.val)
                return max(node.val, node.val + max_left)
            else:
                ans = max(
                    ans,
                    max_right + max_left + node.val,
                    node.val,
                    max_left + node.val,
                    max_right + node.val,
                )
                return max(
                    # max_right + max_left + node.val,  # * Include BOTH
                    node.val,  # * Include NOTHING
                    max_left + node.val,  # * Include ONLY LEFT
                    max_right + node.val,  # * Include ONLY RIGHT
                )

        helper(root)
        return ans

