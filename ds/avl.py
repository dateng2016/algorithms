from typing import Optional


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def insert(self, root: Optional[Node], key):
        # * DO the inserting and then recursively check balance
        # * from BOTTOM to UP

        # 1. Perform the normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # 2. Update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # 3. Get the balance factor
        balance = self.get_balance(root)

        # 4. If the node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # return the (unchanged) node pointer
        return root

    def left_rotate(self, z: Optional[Node]):
        y: Node = z.right  # * y is the PIVOT POINT
        T2 = y.left  # * the OLD left child of PIVOT POINT

        # Perform rotation
        y.left = z
        z.right = T2  # * the OLD left child becomes the NEW right child of "ROOT" Node

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y  # * NEW ROOT

    def right_rotate(self, z: Optional[Node]):
        # * Similarly to before except in reverse order
        y: Node = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, node: Node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, node: Node):
        if not node:
            return
        print(f"{node.key} ", end="")
        self.pre_order(node.left)
        self.pre_order(node.right)


# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl_tree.insert(root, key)

    print("Pre-order traversal of the constructed AVL tree:")
    avl_tree.pre_order(root)
    print()

