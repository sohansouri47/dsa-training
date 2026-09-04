# Learnings

## Things That Clicked

- The 3-step rule for star patterns works perfectly:
  1. Outer loop counts the number of lines.
  2. Inner loop focuses on columns and builds a relationship with the rows.
  3. Print the character inside the inner loop.
- In recursion, placing operations *after* the recursive call allows execution in reverse order (backtracking/unwinding) since it relies on the call stack.
- Parameterized recursion vs Functional recursion: Parameterized passes the accumulator state forward, functional passes the return values backward.

## Implementation Mistakes

- I found functional recursion harder to implement than parameterized recursion because thinking about returning the multiplied value backward is less intuitive than passing the accumulator forward.
- I completely didn't know we have to write a return for a recursive call when using functional recursion.
- Still need to work on generating subsequences (Take/Not Take). I drew the recursion tree on paper which helped, but need to habituate functional recursion. Parameterized recursion feels better.
- **Focus & Burnout**: Don't put legs in multiple problems, especially when tired. Trying to build a recursive base requires focus. If tired, picking one problem and fully understanding it is better than skimming many and getting confused.
- **Recursion vs DP**: Sometimes a recursive solution is correct but not optimal (time limit exceeded). Misunderstanding a subset sum problem as an increasing subsequences problem led to a correct recursive solution, but recognizing when Dynamic Programming is actually required is the next step.
