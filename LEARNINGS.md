# Learnings

## Things That Clicked

- The 3-step rule for star patterns works perfectly:
  1. Outer loop counts the number of lines.
  2. Inner loop focuses on columns and builds a relationship with the rows.
  3. Print the character inside the inner loop.
- In recursion, placing operations *after* the recursive call allows execution in reverse order (backtracking/unwinding) since it relies on the call stack.
- Parameterized recursion vs Functional recursion: Parameterized passes the accumulator state forward, functional passes the return values backward.
- **BFS Visited Timing**: A node MUST be marked visited when *enqueued/discovered*, not when dequeued. Delaying visited marking lets multiple parents enqueue the same child before either is processed.
- **Node ID vs Adjacency List**: `u` is the node ID; `adj[u]` is its list of neighbors. Don't compare a node index with a visited flag (`n != visited[n]`).
- **DFS Iterative Stack LIFO Reversal**: A stack is LIFO, so pushing neighbors `[1, 2, 3]` processes `3` first. To match standard recursive traversal order, push neighbors in reverse: `reversed(adj[node])`.
- **DFS Visited on Pop vs Push**: When marking visited upon pop to match recursive-style judge outputs, multiple copies of a node can enter the stack. Always skip already-visited nodes right after popping (`if visited[node]: continue`).
- **Natural Algorithm Fit**: DFS maps cleanly to recursion via the call stack. BFS fundamentally requires a FIFO queue and is best written iteratively.
- **Grid Traversal Offsets**: Direction arrays (`varx = [1, -1, 0, 0]`, `vary = [0, 0, 1, -1]`) simplify exploring 4-directional neighbors on a 2D matrix.
- **Preserving Original State During In-Place Mutation**: When a traversal modifies the grid as it runs (e.g. changing pixels to a new color), save the source cell's initial value upfront (`ocolor = image[sr][sc]`) so neighbor expansion checks compare against the true starting value.
- **Graph Traversal Complexity is $O(V + E)$, NOT $O(V \cdot E)$**: Traversal visits each vertex once ($O(V)$). Across all vertices, the neighbor loops iterate through the adjacency lists, examining each undirected edge exactly twice ($2E$). The work is summed across all vertices, not repeated $V$ times per edge.
- **Auxiliary vs Total Space**: Traversal auxiliary memory is $O(V)$ (for the `visited` array and DFS recursion stack or BFS queue), while total memory including the graph representation (`adj`) is $O(V + E)$.

## Implementation Mistakes

- I found functional recursion harder to implement than parameterized recursion because thinking about returning the multiplied value backward is less intuitive than passing the accumulator forward.
- I completely didn't know we have to write a return for a recursive call when using functional recursion.
- Still need to work on generating subsequences (Take/Not Take). I drew the recursion tree on paper which helped, but need to habituate functional recursion. Parameterized recursion feels better.
- **Focus & Burnout**: Don't put legs in multiple problems, especially when tired. Trying to build a recursive base requires focus. If tired, picking one problem and fully understanding it is better than skimming many and getting confused.
- **Recursion vs DP**: Sometimes a recursive solution is correct but not optimal (time limit exceeded). Misunderstanding a subset sum problem as an increasing subsequences problem led to a correct recursive solution, but recognizing when Dynamic Programming is actually required is the next step.
- **Queue Efficiency in Python**: Using `list.pop(0)` is $O(n)$ because Python shifts the entire array. Need to habituate `from collections import deque` and `popleft()` for $O(1)$ operations.
- **Traversal From Scratch**: Intuition for BFS/DFS is understood, but both iterative and recursive implementations still require deliberate repetition to write fluently without hints or minor state bugs.
- **Grid Boundary Checks**: Be vigilant with matrix boundaries: allow 0 (`cr >= 0 and cc >= 0` rather than `> 0`), and keep row count (`len(image)`) and column count (`len(image[0])`) distinct.
- **Search Condition Direction**: Watch out for flipped logic/negation bugs (e.g. writing `image[cr][cc] != ocolor` when we want to expand into cells *matching* `ocolor`).
- **Initial Grid Visited State**: In grid BFS, mark the starting cell `(sr, sc)` as visited immediately when creating the queue to prevent cycles/re-enqueueing.
