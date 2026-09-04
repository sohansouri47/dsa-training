"""
Problem: Increasing Subsequences
Topic: Recursion
Pattern: Take/Not Take

First Attempt: A
Current: A

Key Insight:
Use the standard Take/Not Take (include/exclude) pattern, but before the 'Take' branch, check if the current element maintains the increasing order (i.e., it is greater than the last element in the temporary list).

Difficulty:
Misunderstood a Subset Sum problem as Increasing Subsequences, but independently figured out the recursive logic for this. Noted that DP is needed for an optimal solution as pure recursion has a very high time complexity.

Time: O(2^n)
Space: O(n) (recursion stack)

First Seen: 2026-09-04
Last Attempt: 2026-09-04
"""
class Solution:
    def __init__(self):
        self.sol = []

    def subset_inc(self, i, arr, temp):
        if i == len(arr):
            self.sol.append(temp.copy())
            return

        # 'Take' branch
        temp.append(arr[i])

        if len(temp) == 1 or temp[-1] > temp[-2]:
            self.subset_inc(i + 1, arr, temp)

        # 'Not Take' branch
        temp.pop()
        self.subset_inc(i + 1, arr, temp)

    def countSub(self, arr):
        self.sol = []
        self.subset_inc(0, arr, [])
        return len(self.sol) - 1
