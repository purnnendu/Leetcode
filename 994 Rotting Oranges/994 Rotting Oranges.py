"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((i,j))
        time = 0
        while stack:
            num = len(stack)
            count = 1
            for _ in range(num):
                r,c = stack.pop(0)
                for dsr, dsc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= dsr < m and 0 <= dsc < n and grid[dsr][dsc] == 1:
                        grid[dsr][dsc] = 2
                        stack.append((dsr, dsc))
                        count = count*0
            if count == 0:
                time += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time
