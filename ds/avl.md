If the right side is heavy ( l - r = -2 ), we do a left rotation

If the left side is heavy ( l - r = 2 ), we do a right rotation

When doing the left rotation, if the current node's right child has a left child, then that left child becomes the current node's right child. (center's left becomes current's right)

Similarly, when doing the right rotation, if the center has a right child, the that right child will become the current node's left child.

### LL Type -> right rotation

### RR Type -> left rotation

### LR Type -> left child do left rotation, self do right rotation

### RL Type -> right child do right rotation, self do left rotation


When multiple ancestors lose balance after one insertion, only adjust the one that is closest to the inserted node.

**When doing the deletion, we need to check balance all the way up to the root node.**
