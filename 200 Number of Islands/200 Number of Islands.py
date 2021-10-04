"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def recurse(grid,r,c):
            grid[r][c] = '0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                recurse(grid,r-1,c)
            if r+1 < len(grid) and grid[r+1][c] == '1':
                recurse(grid,r+1,c)
            if c-1 >= 0 and grid[r][c-1] == '1':
                recurse(grid,r,c-1)
            if c+1 < len(grid[0]) and grid[r][c+1] == '1':
                recurse(grid,r,c+1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    recurse(grid,i,j)
        return count
