"""
Problem: Array Reversal (Append)
Topic: Recursion
Pattern: Parameterized Recursion

First Attempt: A
Current: A

Key Insight:
Traverse the array recursively and append elements to a new list on the way back (backtracking phase).

Difficulty:
Easy

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
# rev=[]
# arr=[1,2,3,4,5]
def arr_rev(arr,i, rev):
    if i>=len(arr):
        return
    
    arr_rev(arr,i+1, rev)
    rev.append(arr[i])

# print(rev)
# arr_rev(arr,0)
# print(rev)

"""
Problem: Array Reversal (In-place Swap)
Topic: Recursion
Pattern: Two Pointers / Recursion

First Attempt: A
Current: A

Key Insight:
Use two pointers (left and right). Swap them and recursively call with l+1 and r-1 until l > r.

Difficulty:
Easy

Time: O(n)
Space: O(n) (Call stack)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
# arr=[1,2,3,4,5]
def swap_ar_rev(arr,l,r):
    if l>r:
        return
    
    swap_ar_rev(arr,l+1,r-1)
    arr[l],arr[r]=arr[r],arr[l]
# swap_ar_rev(arr,0,len(arr)-1)
# print(arr)

"""
Problem: Palindrome Check
Topic: Recursion
Pattern: Functional Recursion / Two Pointers

First Attempt: D
Current: C

Key Insight:
You MUST return the result of the recursive call. If characters match, return the result of the smaller subproblem.

Difficulty:
Tried after watching video. Forgot to return the recursive call.

Time: O(n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
# i=0
def functional_palindrome(strs,i):
    if i>=len(strs)//2:
        return True
    if strs[i]!=strs[len(strs)-i-1]:
        return False
    return functional_palindrome(strs,i+1)

# print(functional_palindrome('ABCBAD',0))

"""
Problem: Fibonacci Number
Topic: Recursion
Pattern: Multiple Recursive Calls

First Attempt: A
Current: A

Key Insight:
A function can make multiple recursive calls. The execution tree branches out.

Difficulty:
Easy

Time: O(2^n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03
"""
def fib(a):
    if a<=1:
        return 1
    return fib(a-1)+fib(a-2)

# print(fib(10))

"""
Problem: Generate All Subsequences
Topic: Recursion
Pattern: Take/Not Take (Include/Exclude)

First Attempt: D
Current: D

Key Insight:
At every element, make two branches: one where the element is included in the current subsequence, and one where it is excluded. Pop the element after the 'include' branch to backtrack.

Difficulty:
Watched YT directly, pretty sure wouldn't get it. Drew the recursion tree on paper.

Time: O(2^n)
Space: O(n)

First Seen: 2026-09-03
Last Attempt: 2026-09-03

Next Revision: 2026-09-05
"""
def subseq(i,res,arr):
    if i==len(arr):
        print(res)
        return
    res.append(arr[i])
    subseq(i+1,res,arr)
    res.pop()
    subseq(i+1,res,arr)
    
# subseq(0,[],[4,1,2,3])
