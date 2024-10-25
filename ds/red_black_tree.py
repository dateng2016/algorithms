class Node:
    def __init__(self, data):
        self.data = data
        self.color = 'red'  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(None)
        self.NIL_LEAF.color = 'black'  # Sentinel NIL leaf is black
        self.root = self.NIL_LEAF

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node  # Tree was empty
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'  # New node is red
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        # Case 2: Node is right child
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3: Node is left child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Case 1: Uncle is red
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        # Case 2: Node is left child
                        node = node.parent
                        self.right_rotate(node)
                    # Case 3: Node is right child
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL_LEAF:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def inorder_helper(self, node):
        if node != self.NIL_LEAF:
            self.inorder_helper(node.left)
            print(node.data, node.color)
            self.inorder_helper(node.right)

    def inorder(self):
        self.inorder_helper(self.root)

# Example Usage
if __name__ == "__main__":
    rbt = RedBlackTree()
    for value in [10, 20, 30, 15, 25]:
        rbt.insert(value)

    print("Inorder Traversal of the Red-Black Tree:")
    rbt.inorder()

