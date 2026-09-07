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

### Mental Model

- Structure: **Queue (FIFO)** + **Visited array** + Result list.
- **Crucial Rule**: Mark nodes visited **when enqueued/discovered**, NOT when dequeued. Marking on dequeue causes shared neighbors to be enqueued multiple times.
- Python note: `list.pop(0)` is $O(n)$; use `collections.deque.popleft()` for $O(1)$ queue operations.

### Representative Problems

- BFS of Graph

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

