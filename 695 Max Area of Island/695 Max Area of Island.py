"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        largest_island = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    land = collections.deque()
                    land.append((row, col))
                    island_size = 0

                    while land:
                        land_row, land_col = land.popleft()
                        island_size += 1

                        if land_row - 1 >= 0 and grid[land_row - 1][land_col] == 1:
                            grid[land_row - 1][land_col] = 0
                            land.append((land_row - 1, land_col))

                        if land_col + 1 < num_cols and grid[land_row][land_col + 1] == 1:
                            grid[land_row][land_col + 1] = 0
                            land.append((land_row, land_col + 1))

                        if land_row + 1 < num_rows and grid[land_row + 1][land_col] == 1:
                            grid[land_row + 1][land_col] = 0
                            land.append((land_row + 1, land_col))

                        if land_col - 1 >= 0 and grid[land_row][land_col - 1] == 1:
                            grid[land_row][land_col - 1] = 0
                            land.append((land_row, land_col - 1))

                    largest_island = max(largest_island, island_size)


        return largest_island
