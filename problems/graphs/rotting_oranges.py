"""
Problem: Rotting Oranges
Topic: Graphs
Pattern: Multi-Source Breadth-First Search

First Attempt: C
Current: C

Key Insight:
Rotting spreads simultaneously from all rotten oranges at t = 0. Enqueue all initial
rotten oranges upfront with time 0 (multi-source BFS). As oranges rot, push neighbors with t + 1
and mark them visited. A final pass checks if any fresh orange was unreachable.

Difficulty:
Needed hints to identify the multi-source BFS pattern and queue structure.
Solved implementation independently after taking conceptual hints.
Note: list.pop(0) is O(n); collections.deque.popleft() is preferred for BFS queue efficiency.

Time: O(m * n)
Space: O(m * n)

First Seen: 2026-09-09
Last Attempt: 2026-09-09

Revision History:
2026-09-09: C

Next Revision: 2026-09-11
"""
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=[[0]*len(grid[0]) for _ in range(len(grid))]
        varsx=[1,-1,0,0]
        varsy=[0,0,1,-1]
        q=[]
        mt=0

        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j,0])
                    visited[i][j]=2

        while len(q)!=0:
            ci,cj,t=q.pop(0)
            mt=max(mt,t)
            for i in range(len(varsx)):
                curi=ci+varsx[i]
                curj=cj+varsy[i]
                if (
                    0 <= curi < len(grid)
                    and 0 <= curj < len(grid[0])
                    and visited[curi][curj] != 2
                    and grid[curi][curj] == 1
                ):
                    q.append([curi,curj,t+1])
                    visited[curi][curj] = 2
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and visited[i][j]!=2:
                    return -1
        return mt
