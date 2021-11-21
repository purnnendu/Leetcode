"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Example 3:

Input: dividend = 0, divisor = 1
Output: 0

Example 4:

Input: dividend = 1, divisor = 1
Output: 1
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 1: #not necessary but makes things simpler
            return dividend
        if dividend == -2**31 and divisor == -1: #accurately deal with overflow
            return 2**31-1
        neg = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        endres = 0
        while dividend >= divisor:
		   #At each iteration subtract the largest possible divisor*r=divisor*(2**k)
            resm = divisor
            r = 1
            while resm + resm < dividend:
                r += r
                resm += resm
            dividend -= resm
            endres += r
        return 0 - endres if neg else endres
