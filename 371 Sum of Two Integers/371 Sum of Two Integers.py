"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # follow up
        # don't use manipulation to handle negative
        # Python has no 32-bit limit so we do that on purpose
        # bitmask of 32 1-bits
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        maxInt = 0x7FFFFFFF
        # in python, negative numbers are represented by infinite number of leading 1s, after the bitwise and with MASK, all the leading 1s are set to be 0s, so python will interpret it as a positive number
        if a < maxInt:
            return a
        else:
            # the extra bit is for negative sign
            return ~ (a ^ mask)
