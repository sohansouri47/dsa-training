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
