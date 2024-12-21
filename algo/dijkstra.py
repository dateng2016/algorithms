import heapq


def dijkstra(graph, start):
    """
    Finds the shortest path from the start node to all other nodes in a weighted graph.

    :param graph: A dictionary where keys are nodes and values are lists of tuples (neighbor, weight).
    :param start: The starting node.

    :return: A dictionary with the shortest distance from start to each node.
    """
    # Priority queue to keep track of the node with the smallest tentative distance
    pq = [(0, start)]  # (distance, node)

    # Dictionary to store the shortest distance from start to each node
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Set to track visited nodes
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip processing if node is already visited
        if current_node in visited:
            continue
        visited.add(current_node)

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue

            new_distance = current_distance + weight

            # Only update the shortest path if we find a shorter distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    return distances


from typing import Dict
import heapq


def dijkstra2(graph: Dict, start_node: str):
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    dist_node = [(0, start_node)]
    while dist_node:
        dist, node = heapq.heappop(dist_node)
        for neighbor, dist_to_neigh in graph[node]:
            total_dist = dist + dist_to_neigh
            if total_dist < distances[neighbor]:
                distances[neighbor] = total_dist
                heapq.heappush(dist_node, (total_dist, neighbor))
    return distances


# Example graph (adjacency list representation)
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)],
}

start_node = "A"
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from {start_node}:")
for node, dist in shortest_paths.items():
    print(f"Distance to {node}: {dist}")
print(dijkstra(graph, node) == dijkstra2(graph, node))
