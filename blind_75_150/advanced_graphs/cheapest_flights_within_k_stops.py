from typing import List
from collections import defaultdict, deque


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # * Gemini Solution
        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((destination, price))

        # min_costs[city][edges_taken] = min_price
        # Using a nested dict for potentially sparse storage
        # Outer key: number of edges, Inner key: city
        # Or: min_costs[(city, edges_taken)] = min_price
        min_costs = defaultdict(lambda: defaultdict(lambda: float("inf")))
        min_costs[src][0] = 0

        # Queue stores: (current_city, edges_taken_to_reach_city, price_to_reach_city)
        q = deque()
        q.append((src, 0, 0))  # city, edges, current_total_price

        cheapest_price_to_dst = float("inf")

        while q:
            city, edges_so_far, price_so_far = q.popleft()

            # If we've already found a path to this state (city, edges_so_far)
            # that's cheaper than price_so_far, then this queue entry is stale.
            if price_so_far > min_costs[city][edges_so_far]:
                continue

            # If we have taken k+1 edges to reach `city`, we cannot take any more edges
            # unless the next hop is the destination.
            # The loop below checks `new_edges = edges_so_far + 1`.
            # If `edges_so_far == k+1`, then `new_edges` would be `k+2`, which is too many.
            # So we can effectively stop exploring from `city` if `edges_so_far > k`.
            # (The only exception is if `city` itself is `dst`, but `dst` is not added to queue for further exploration usually)
            if edges_so_far > k:  # Path to `city` uses > k edges (i.e., >= k+1 edges)
                # Next hop would make it > k+1 edges.
                continue

            for next_city, leg_price in graph[city]:
                new_total_price = price_so_far + leg_price
                new_edges_count = edges_so_far + 1

                if new_total_price < min_costs[next_city][new_edges_count]:
                    min_costs[next_city][new_edges_count] = new_total_price
                    # No need to check new_edges_count against k+1 here for adding to queue
                    # because the check `if edges_so_far > k: continue` at the start of the
                    # while loop (when this new state is popped) will handle it.
                    # Or, add a check here: if new_edges_count <= k+1 and next_city != dst:
                    q.append((next_city, new_edges_count, new_total_price))

                # Regardless of pruning for queue, if next_city is dst, update overall min
                if (
                    next_city == dst and new_edges_count <= k + 1
                ):  # Path to dst must be within k+1 edges
                    if new_total_price < cheapest_price_to_dst:
                        cheapest_price_to_dst = new_total_price

        return cheapest_price_to_dst if cheapest_price_to_dst != float("inf") else -1
