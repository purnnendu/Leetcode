"""
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:

Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def helper(x, y, moves):
            if x == m or y == n or x < 0 or y < 0:
                return 1

            if moves == 0:
                return 0

            ans = helper(x - 1, y, moves - 1)
            ans += helper(x, y - 1, moves - 1)
            ans += helper(x + 1, y, moves - 1)
            ans += helper(x, y + 1, moves - 1)

            return ans % MOD

        MOD = 10**9 + 7

        return helper(startRow, startColumn, maxMove)
