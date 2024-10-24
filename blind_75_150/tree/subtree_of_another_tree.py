from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(node1: TreeNode, node2: TreeNode) -> bool:
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        # Traverse the original tree to see if there is a match???
        # R -> O(S T) Where S T represents the number of nodes for the
        #       two trees
        def helper(root: TreeNode, subRoot: TreeNode):
            if not root and subRoot:
                return False
            if check(root, subRoot):
                return True
            return helper(root.left, subRoot) or helper(root.right, subRoot)

        return helper(root, subRoot)



