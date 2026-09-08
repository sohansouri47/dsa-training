"""
Problem: Flood Fill
Topic: Graphs
Pattern: Breadth-First Search

First Attempt: C
Current: C

Key Insight:
Flood fill traverses connected cells of the same initial color like BFS on a grid.
Record the starting cell's original color before making modifications, and only spread to neighbors
that match the original color. Mark cells visited as soon as they are added to the queue to prevent duplicate enqueues.

Difficulty:
Required hints across several areas:
1. Boundary condition including index 0 (cr >= 0 and cc >= 0).
2. Distinguishing row count len(image) from column count len(image[0]).
3. Saving and comparing against starting cell's original color rather than hardcoded 1 or new color.
4. Marking cells visited upon enqueue rather than dequeue.
5. Marking starting cell (sr, sc) visited initially upon queue creation.
6. Inverted condition bug: wrote image[cr][cc] != ocolor instead of == ocolor.
Note: list.pop(0) is O(n); collections.deque.popleft() is preferred for BFS queue efficiency.

Time: O(m * n)
Space: O(m * n)

First Seen: 2026-09-08
Last Attempt: 2026-09-08

Revision History:
2026-09-08: C

Next Revision: 2026-09-10
"""
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[0] * len(image[0]) for _ in range(len(image))]
        q = [[sr, sc]]
        visited[sr][sc] = 1
        varx = [1, -1, 0, 0]
        vary = [0, 0, 1, -1]
        cr, cc = 0, 0
        ocolor = image[sr][sc]
        if image[sr][sc] == color:
            return image
        while len(q) != 0:
            x, y = q.pop(0)
            image[x][y] = color

            for i in range(len(varx)):
                cr = x + varx[i]
                cc = y + vary[i]
                if (
                    cr >= 0
                    and cc >= 0
                    and cr < len(image)
                    and cc < len(image[0])
                    and image[cr][cc] != ocolor
                    and visited[cr][cc] != 1
                ):
                    q.append([cr, cc])
                    visited[cr][cc] = 1
            print(q)
        return image
