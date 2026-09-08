"""
Problem: Connected Components in an Undirected Graph
Topic: Graphs
Pattern: Connected Components

First Attempt: A
Current: A

Key Insight:
An outer loop iterates through all vertices 0 to V - 1. For each unvisited vertex, initiate a DFS (or BFS)
to traverse the entire connected subgraph and mark all reachable nodes as visited, collecting each component.
Time complexity is O(V + E) because each vertex is visited once and each undirected edge is checked twice
across all adjacency lists combined, NOT O(V * E).

Difficulty:
None. Cleanly constructed adjacency list and applied DFS to traverse components.
Demonstrated clear understanding that auxiliary space is O(V) (visited array + recursion stack)
while total space is O(V + E) including the adjacency list.

Time: O(V + E)
Space: O(V + E) (Auxiliary: O(V))

First Seen: 2026-09-08
Last Attempt: 2026-09-08

Revision History:
2026-09-08: A

Next Revision: 2026-09-10
"""
from typing import List

class Solution:
    def findConnectedComponents(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * V
        components = []

        def dfs(node, component):
            visited[node] = 1
            component.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i in range(V):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)

        return components
