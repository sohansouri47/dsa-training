"""
Problem: Print Name 5 Times
Topic: Recursion
Pattern: Basic Recursion

First Attempt: A
Current: A

Key Insight:
Use a base condition to return when the target number is reached.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def print_5(a):
    if a==5:
        return
    print("hello")
    a+=1
    print_5(a)

# print_5(0)


"""
Problem: Linear Print 1 to N
Topic: Recursion
Pattern: Basic Recursion

First Attempt: A
Current: A

Key Insight:
Print the value, then increment and make the recursive call.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def linear_print(a):
    if a==10:
        return 
    print(a)
    a+=1
    linear_print(a)

# linear_print(0)


"""
Problem: Linear Print N to 1
Topic: Recursion
Pattern: Basic Recursion

First Attempt: A
Current: A

Key Insight:
Print the value, then decrement and make the recursive call.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def r_linear_print(a):
    if a==0:
        return
    print(a)
    a-=1
    r_linear_print(a)
# r_linear_print(10)


"""
Problem: Linear Print 1 to N (Backtracking)
Topic: Recursion
Pattern: Backtracking

First Attempt: A
Current: A

Key Insight:
Make the recursive call first, then print after the call returns. The call stack handles the reversal.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def r_backtrack_linear_print(a):
    if a>3:
        return
    elif a<=3:
        a+=1
        r_backtrack_linear_print(a)
    print(a)

# r_backtrack_linear_print(0)


"""
Problem: Linear Print N to 1 (Backtracking)
Topic: Recursion
Pattern: Backtracking

First Attempt: A
Current: A

Key Insight:
Make the recursive call by decrementing first, then print after the return.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def backtrack_linear_print(a):
    if a<=1:
        return
    elif a>0:
        a-=1
        backtrack_linear_print(a)
    print(a)

# backtrack_linear_print(5)


"""
Problem: Factorial (Functional vs Parameterized)
Topic: Recursion
Pattern: Functional vs Parameterized Recursion

First Attempt: A
Current: A

Key Insight:
Functional recursion relies on returning a value that multiplies with the result of the recursive call. Parameterized recursion passes the accumulator down to the next call.

Difficulty:
Easy.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def functional_factorial(a):
    if a==1:
        return a
    return a*functional_factorial(a-1)
# print(functional_factorial(5))

def para_factorial(a,fact):
    if a==5:
        print(fact)
        return 
    para_factorial(a+1,(a+1)*fact)
    
# para_factorial(1,1)
