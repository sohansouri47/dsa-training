"""
Problem: Adjacency Matrix to Adjacency List
Topic: Graphs
Pattern: Graph Representation

First Attempt: C
Current: B

Key Insight:
For every cell matrix[i][j] == 1, there is a directed edge from i to j.
Iterate through the matrix and append j to adj[i].

Difficulty:
Learned the conversion logic and distinction between adjacency matrix and adjacency list representation.

Time: O(V^2)
Space: O(V + E)

First Seen: 2026-09-07
Last Attempt: 2026-09-07

Next Revision: 2026-09-09
"""
def matrix_to_list(matrix):
    n = len(matrix)
    adj = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                adj[i].append(j)

    return adj


"""
Problem: BFS of Graph
Topic: Graphs
Pattern: Breadth-First Search

First Attempt: C
Current: B

Key Insight:
A node must be marked visited when it is enqueued/discovered, NOT when it is dequeued.
If marked on dequeue, shared neighbors in diamond structures get enqueued multiple times.

Difficulty:
Initial bugs included confusing adj[0] with node 0, comparing node number against visited flag,
marking visited too late, and duplicate node 0 insertion. Corrected after targeted hints.
Note: list.pop(0) is O(n); collections.deque.popleft() is preferred for production.

Time: O(V + E)
Space: O(V)

First Seen: 2026-09-07
Last Attempt: 2026-09-07

Next Revision: 2026-09-09
"""
class SolutionBFS:
    # Iterative BFS
    def bfs(self, adj):
        queue = [0]
        visited = [0] * len(adj)
        res = []

        visited[0] = 1

        while queue:
            cur_node = queue.pop(0)
            res.append(cur_node)

            for neighbor in adj[cur_node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    queue.append(neighbor)

        return res

    # Recursive BFS exploration
    def bfs_recursive(self, adj):
        visited = [0] * len(adj)
        res = []
        queue = [0]

        visited[0] = 1

        def helper():
            if not queue:
                return

            node = queue.pop(0)
            res.append(node)

            for neighbor in adj[node]:
                if visited[neighbor] == 0:
                    visited[neighbor] = 1
                    queue.append(neighbor)

            helper()

        helper()
        return res


"""
Problem: DFS of Graph
Topic: Graphs
Pattern: Depth-First Search

First Attempt: C
Current: B

Key Insight:
DFS naturally maps to recursion via the call stack. For iterative DFS with an explicit stack,
LIFO behavior processes neighbors in reverse, so push neighbors in reversed order.
To match recursive DFS ordering expected by judges, mark visited upon pop and skip already-visited nodes.

Difficulty:
Encountered stack LIFO ordering differences, missed initial visited marking for node 0,
and handled differences between visited-on-push vs visited-on-pop.

Time: O(V + E)
Space: O(V)

First Seen: 2026-09-07
Last Attempt: 2026-09-07

Next Revision: 2026-09-09
"""
class SolutionDFS:
    # Iterative DFS (Visited on pop, reversed neighbors)
    def dfs_iterative(self, adj):
        stack = [0]
        visited = [0] * len(adj)
        res = []

        while stack:
            cur_node = stack.pop()

            if visited[cur_node] == 1:
                continue

            visited[cur_node] = 1
            res.append(cur_node)

            for neighbor in reversed(adj[cur_node]):
                if visited[neighbor] == 0:
                    stack.append(neighbor)

        return res

    # Recursive DFS
    def dfs(self, adj):
        visited = [0] * len(adj)
        res = []

        def helper(node):
            visited[node] = 1
            res.append(node)

            for neighbor in adj[node]:
                if visited[neighbor] == 0:
                    helper(neighbor)

        helper(0)
        return res
