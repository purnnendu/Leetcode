"""
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        sqr = sqrt(n)
        pool = {i**2 for i in range(int(sqr)+1)}
        test = [i**2 for i in range(int(sqr*0.71)+1)]

        for i in test:
            for j in test:
                if n-i-j in pool:
                    return 3-(i==0)-(j==0)
        return 4
