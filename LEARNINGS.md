# Learnings

## Things That Clicked

- The 3-step rule for star patterns works perfectly:
  1. Outer loop counts the number of lines.
  2. Inner loop focuses on columns and builds a relationship with the rows.
  3. Print the character inside the inner loop.
- In recursion, placing operations *after* the recursive call allows execution in reverse order (backtracking/unwinding) since it relies on the call stack.
- Parameterized recursion vs Functional recursion: Parameterized passes the accumulator state forward, functional passes the return values backward.
