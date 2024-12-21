#
# * DFS Approach
def topological_sort_dfs(graph):
    """
    Perform topological sort on a directed acyclic graph using DFS.

    :param graph: A dictionary where keys are nodes and values are lists of neighbors.
    :return: A list of nodes in topologically sorted order.
    """
    visited = set()  # To keep track of visited nodes
    stack = []  # To store the topological sort
    temp_stack = (
        set()
    )  # To track nodes currently in the recursion stack (for cycle detection)

    def dfs(node):
        if node in temp_stack:
            raise ValueError("Graph contains a cycle!")
        if node not in visited:
            visited.add(node)
            temp_stack.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            temp_stack.remove(node)
            stack.append(node)
            # * Here the stack has the property where the last
            # * one has the least incoming edges

    # Perform DFS for each node in the graph
    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Reverse the stack to get the correct topological order


# Example graph (adjacency list representation)
graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I"],
    "E": [],
    "F": ["I"],
    "G": [],
    "H": ["I"],
    "I": [],
}


sorted_order = topological_sort_dfs(graph)
print("Topological Sort (DFS-based):", sorted_order)


# * BFS Approach (Kahn's algorithm)
from collections import deque, defaultdict


def topological_sort_kahn(graph):
    """
    Perform topological sort on a directed acyclic graph using Kahn's Algorithm (BFS).

    :param graph: A dictionary where keys are nodes and values are lists of neighbors.
    :return: A list of nodes in topologically sorted order.
    """
    in_degree = defaultdict(int)  # To store in-degree of each node
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    # Queue for nodes with zero in-degree
    queue = deque([node for node in graph if in_degree[node] == 0])

    top_order = []

    while queue:
        node = queue.popleft()
        top_order.append(node)

        # Decrease the in-degree of each neighbor and add it to queue if it becomes 0
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the number of nodes in top_order is less than the number of nodes in the graph,
    # it means there is a cycle.
    if len(top_order) != len(graph):
        raise ValueError("Graph contains a cycle!")

    return top_order


# Example graph (adjacency list representation)
graph = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G", "H"],
    "D": ["I"],
    "E": [],
    "F": ["I"],
    "G": [],
    "H": ["I"],
    "I": [],
}

sorted_order = topological_sort_kahn(graph)
print("Topological Sort (Kahn's Algorithm):", sorted_order)
