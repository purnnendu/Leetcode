"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5

Example 2:

Input: n = 1
Output: 1
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = { 0:1, 1:1 }
        for x in range(2,n+1):
            dp[x] = 2 * sum([ dp[y]*dp[x-y-1] for y in range(x//2) ] )
            if x%2:
                dp[x] += dp[x//2]**2
        return dp[n]
