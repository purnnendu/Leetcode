"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        i = 1  # -> set up the left bound 1
        j = x   # -> set up the upper open bound x, because we have taken the corner case x == 0 or 1 into consider
        while i < j:   # -> node that the searching space is [1, x)
            mid = (i + j) // 2
            if mid * mid > x:   # -> This is our g(m), our goal is to find a point, mid,  where mid is the first element that satisfy mid**mid > x.
                j = mid
            else:
                i = mid + 1
        return i - 1   # -> note that j is the first element that is larger than x, so we just need to subtract by 1 to get the result we want
