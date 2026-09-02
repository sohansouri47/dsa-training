"""
Problem: Patterns 1-12
Topic: Basics
Pattern: Star Patterns

First Attempt: A
Current: A

Key Insight:
For the outer loop count the number of lines. For the inner loop focus on columns and build relationship with rows. Print the star inside the inner for loop.

Difficulty:
None. Was able to solve independently by following the 3 step rule.

Time: O(n^2) for most patterns
Space: O(1)

First Seen: 2026-09-02
Last Attempt: 2026-09-02

Revision History:
2026-09-02: A

Next Revision: None
"""

def pattern1(n):
    for i in range(n):
        print("*" * n)

def pattern2(n):
    for i in range(1, n + 1):
        print("*" * i)

def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()

def pattern5(n):
    for i in range(n, 0, -1):
        print("*" * i)

def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def pattern7(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1) + " " * (n - i - 1))

def pattern8(n):
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1) + " " * i)

def pattern9(n):
    pattern7(n)
    pattern8(n)

def pattern10(n):
    for i in range(1, 2 * n):
        stars = i
        if i > n:
            stars = 2 * n - i
        print("*" * stars)

def pattern11(n):
    for i in range(1, n + 1):
        start = 1 if i % 2 != 0 else 0
        for j in range(i):
            print(start, end="")
            start = 1 - start
        print()

def pattern12(n):
    space = 2 * (n - 1)
    for i in range(1, n + 1):
        # numbers
        for j in range(1, i + 1):
            print(j, end="")
        # spaces
        print(" " * space, end="")
        # numbers
        for j in range(i, 0, -1):
            print(j, end="")
        print()
        space -= 2
