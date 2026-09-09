# Patterns Library

## Star Patterns

### Recognition Signals

- Drawing shapes with characters (stars, numbers)
- Need to print in rows and columns

### Mental Model

- Outer loop counts the number of lines (rows).
- Inner loop focuses on the columns and builds a relationship with the rows (e.g. number of columns depends on current row).
- Print the character inside the inner loop.

### Representative Problems

- Patterns 1-12

## Basic Recursion & Backtracking

### Recognition Signals

- Problem involves repeating a similar operation with a smaller or modified input.
- Need to build a sequence of operations that unwind (Backtracking).

### Mental Model

- Every recursive function must have a **base condition** to stop.
- In basic recursion, you do the work before the recursive call.
- In backtracking (or unwinding), you make the recursive call first, and do the work after it returns.

### Representative Problems

- Linear Print 1 to N
- Factorial

## Take/Not Take (Subsequences)

### Recognition Signals

- Need to generate all possible combinations or subsequences of an array or string.
- Subsets/Subsequences are requested.

### Mental Model

- At each element in the input, the recursive function branches into two paths:
  1. **Take** the element (add to current result).
  2. **Not Take** the element (skip it).
- Use a list to build the subsequence and `.pop()` to backtrack when coming back from the "Take" branch.

### Representative Problems

- Generate All Subsequences

## Multiple Recursive Calls

### Recognition Signals

- The problem naturally breaks down into multiple smaller subproblems of the same type.
- Example: Fibonacci sequence, where F(n) depends on both F(n-1) and F(n-2).

### Mental Model

- A function can make multiple recursive calls, which creates a branching execution tree rather than a straight line.
- The base conditions must handle all valid stopping points for the tree.

### Representative Problems

- Fibonacci Number

## Graph Representation

### Recognition Signals

- Problem provides network connections, edge pairs, or grid adjacency.
- Need efficient neighbor traversal for sparse graphs.

### Mental Model

- **Adjacency List (`adj`)**: An array/dictionary of lists where `adj[u]` holds direct neighbors of `u`. Preferred for $O(V + E)$ space and fast iteration.
- **Adjacency Matrix (`matrix`)**: A 2D array where `matrix[i][j] == 1` indicates a directed edge $i \to j$. $O(1)$ edge lookup, but $O(V^2)$ space.

### Representative Problems

- Adjacency Matrix to Adjacency List

## Breadth-First Search (BFS)

### Recognition Signals

- Need level-by-level or equidistant traversal outward from a source.
- Finding shortest path or minimum steps in an unweighted graph.
- Exploring connected components on a 2D matrix/grid (e.g., flood fill, islands).

### Mental Model

- Structure: **Queue (FIFO)** + **Visited array** + Result / Mutation.
- **Crucial Rule**: Mark nodes visited **when enqueued/discovered**, NOT when dequeued. Also mark the start cell/node visited upon initial enqueue.
- **Grid Traversal**: Use coordinate offset vectors (`varx = [1, -1, 0, 0]`, `vary = [0, 0, 1, -1]`) to cleanly visit 4-directional neighbors.
- **Grid Boundaries**: Check `0 <= cr < len(image)` (rows) and `0 <= cc < len(image[0])` (columns).
- **In-Place Mutation**: Save starting state (`ocolor = image[sr][sc]`) before modifying cells so neighbor validation checks against the original value.
- Python note: `list.pop(0)` is $O(n)$; use `collections.deque.popleft()` for $O(1)$ queue operations.

### Representative Problems

- BFS of Graph
- Flood Fill

## Depth-First Search (DFS)

### Recognition Signals

- Need to explore each path completely before backtracking.
- Connected components, cycle detection, path existence.

### Mental Model

- Maps naturally to **Recursion** via the call stack (processes neighbors in adjacency order).
- **Iterative DFS (Stack / LIFO)**: Stack reverses order; push neighbors in reverse (`reversed(adj[u])`) to match recursive traversal order.
- Visited Timing: When marking visited on pop (to mimic recursion order), stack may hold duplicate references—always skip already visited nodes upon popping (`if visited[node]: continue`).

### Representative Problems

- DFS of Graph

## Connected Components

### Recognition Signals

- Finding isolated subgraphs, clusters, or groupings of mutually reachable vertices in an undirected graph.
- Problem asks to count provinces, disconnected networks, or group connected entities.

### Mental Model

- **Outer Loop Traversal**: Iterate over all vertices $i \in [0, V-1]$. If vertex $i$ is unvisited, launch a DFS (or BFS) from $i$ to traverse and mark the entire connected component.
- **Count / Collect**: Each time an unvisited vertex triggers a traversal from the outer loop, increment component count or collect the component list.
- **Time Complexity — $O(V + E)$**: Every vertex is visited once. Across all vertices, every undirected edge is checked twice ($2E$, once from each endpoint in the adjacency list). It is NOT $O(V \cdot E)$, which would mean scanning all edges for every vertex.
- **Space Complexity**: Auxiliary space is $O(V)$ (visited array + recursion stack / queue); total space is $O(V + E)$ including the adjacency list.

### Representative Problems

- Connected Components in an Undirected Graph

## Multi-Source Breadth-First Search (BFS)

### Recognition Signals

- Multiple starting sources expand, spread, or infect outward simultaneously at time $t = 0$.
- Finding minimum time or steps for a spread effect to cover all reachable cells in a grid.
- Keywords/themes: rotting oranges spreading, fire spreading, water flooding from multiple sources.

### Mental Model

- **Simultaneous Initialization**: Scan the grid and enqueue **all** starting sources at $t = 0$ upfront before starting the BFS loop.
- **Queue Tuple `[row, col, time]`**: Store the timestamp directly in each queue node to naturally track elapsed time without separate layer delimiters.
- **Mark Visited Upon Enqueue**: Mark cells visited (e.g. `visited[cr][cc] = 2`) immediately when enqueuing with `t + 1` to prevent duplicate neighbor additions.
- **Post-Traversal Completeness Check**: After the queue empties, do a full pass over the grid to verify whether any target cells remain unaffected (`grid[i][j] == 1 and visited[i][j] != 2`), returning `-1` if unreachable.
- Python efficiency note: Use `collections.deque.popleft()` instead of `list.pop(0)` for $O(1)$ queue operations.

### Representative Problems

- Rotting Oranges


