import json


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    """NEETCODE GUY"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def pre_order(node: TreeNode):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            pre_order(node.left)
            pre_order(node.right)

        pre_order(root)
        return ",".join(res)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        self.idx = 0

        def dfs():
            if arr[self.idx] == "N":
                self.idx += 1
                return None
            val = int(arr[self.idx])
            node = TreeNode(val)
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# class Codec:

# def serialize(self, root: TreeNode) -> str:
#     """Encodes a tree to a single string.

#     :type root: TreeNode
#     :rtype: str
#     """
#     res = []

#     def helper(node: TreeNode, idx: int, level: int):
#         if not node:
#             return
#         if idx >= len(res):
#             # * We need to expand the "res" array
#             for _ in range(2**level):
#                 res.append(None)

#         res[idx] = node.val
#         helper(node.left, 2 * idx + 1, level + 1)
#         helper(node.right, 2 * idx + 2, level + 1)

#     helper(root, 0, 0)
#     # print(res)
#     return json.dumps(res)

# def deserialize(self, data: str) -> TreeNode:
#     """Decodes your encoded data to tree.

#     :type data: str
#     :rtype: TreeNode
#     """
#     arr = json.loads(data)
#     # print(f"arr: {arr}, {type(arr[0])}")
#     l = len(arr)

#     def helper(idx):
#         if idx >= l or arr[idx] == None:
#             # print(idx)
#             return None
#         left_idx = 2 * idx + 1
#         right_idx = 2 * idx + 2
#         root = TreeNode(arr[idx])
#         root.left = helper(left_idx)
#         root.right = helper(right_idx)
#         return root

#     return helper(0)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

