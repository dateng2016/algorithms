## Attributes

-   Order m -> m-way B-tree (maximum number of branches allowed)
-   Maximum
    -   Allow (m - 1) elements for each node at maximum, m branches
-   Minimum
    -   For root node, it has to have at least 1 element, two branches
    -   For other node, it has to have at least ceil(m / 2) branches and (ceil ( m / 2 )) elements

## Insert

-   The insertion point will always land on the leaf node. If no overflow happens, we leave it as is.
-   When overflow happens, get the middle index (_mid_ cannot be smaller than len / 2, 1-indexed. EX: len = 5 -> third element, len = 4 -> 2 element), split it into left and right part, move the _mid_ element up one level. _left_ and _right_ becomes two nodes. Do this recursively upwards until no overflow happens. (It is possible that we apply this method to the root node as well.)

## Delete

-   If no underflow happens, leave it as is
-   **LEAF NODE**
    -   check the _left brother_ and _right brother_ to see if they have any that the current node can borrow.
        -   If they CAN borrow -> Do a clock/counter-clock wise rotation that involves the `brother node element`, `father node element`, and `current node` (**Father down, brother up**)
        -   They CANNOT borrow -> move the corresponding elements from father down, then MERGE
-   ## **NON-LEAF NODE**
    -   Delete it and then use its _predecessor_ or _successor_ to replace it
        -   If underflow occurs on the leaf node, do the above operation for LEAF NODE
    -   If the father node underflows after merging, borrowf from brother?
        -   If brother can borrow, borrow from brother
        -   If not, Merge with the brother

`Note: `Predecessor is the MAX value of the LEFT subtree and Successor is the MIN value of the RIGHT subtree
