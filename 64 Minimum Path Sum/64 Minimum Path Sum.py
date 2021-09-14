"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # get dimensions
        n = len(grid) # no of cells in each col
        m = len(grid[0]) # no of cells in each row

        # populate first row using m for no of cells in row
        for i in range(1,m):
            grid[0][i] = grid[0][i] + grid[0][i-1]

        # populate first col using n for no of cells in col
        for j in range(1,n):
            grid[j][0] = grid[j-1][0] + grid[j][0]

        # populate the rest
        for i in range(1,n):
            for j in range(1,m):
				# get min seen so far plus curr cell value
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]

        # return last cell
        return grid[-1][-1]
