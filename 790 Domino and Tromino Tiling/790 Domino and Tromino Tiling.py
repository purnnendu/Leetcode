"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

Example 1:

Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1
"""
class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        if n == 3:
            return 5
        arr = [0] * (n+1)
        arr[1], arr[2], arr[3], mod = 1, 2, 5, 1000000007
        for i in range(4, n+1):
            arr[i] = ((2*arr[i-1])%mod + arr[i-3]%mod)%mod
        return arr[n]
