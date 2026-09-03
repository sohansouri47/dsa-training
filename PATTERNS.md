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
