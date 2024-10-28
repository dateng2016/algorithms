### RULES:

1. It has to be a binary search tree
2. ROOT and LEAF (NULL) have to be black
3. No two adjacent red nodes
4. Paths from any node to its leaf nodes have the same length

Feature:
The longest path is no longer than twice of the shortest path.

When inserting, default it to RED.

### Three conditions when balance is lost

1. The node inserted is the root node

-   Turn it BLACK

2. The UNCLE of the inserted node is RED

-   Grandpa, Father, Uncle ALL change color -> Grandpa becomes the inserted node -> recursively check if the balance is lost and act accordingly

3. The UNCLE of the inserted node is BLACK

-   Rotate according to (LL, RR, LR, RL) in AVL tree. Then change color of the PIVOTING NODE and ROTATING NODE of the LAST ROTATION
