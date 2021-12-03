"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        # If board have less than 3 size in any direction: nothing to do, because all cells located on borders
        if n < 3 or m < 3:
            return

        # DFS to look for the next 'O' cell upper, lower, to the right and to the left of current coordinates
        # If 'O' cell is found, recursevly mark this cell as 'R' which is mean REACHED
        def dfs(row: int, col: int) -> None:
            board[row][col] = 'R'
            if row > 0 and board[row - 1][col] == 'O':
                dfs(row - 1, col)
            if row < n - 1 and board[row + 1][col] == 'O':
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == 'O':
                dfs(row, col - 1)
            if col < m - 1 and board[row][col + 1] == 'O':
                dfs(row, col + 1)

        # Go and check left and right borders of the board
        for row in range(n):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][m - 1] == 'O':
                dfs(row, m - 1)

        # Same for check up and down borders of the board
        # Since corners (0,0) and (n - 1, m - 1) where checked in previous cycle, skip them in this one
        for col in range(1, m - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[n - 1][col] == 'O':
                dfs(n - 1, col)

        # Follow through the whole board and flip all 'R' cells back into 'O' and all 'O' cell to 'X'
        # since they're unreacheable from the board located 'O' cell if any
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O'
