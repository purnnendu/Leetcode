"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537
"""
from functools import lru_cache

@lru_cache(None)
def trib(n):
    if n <= 2:
        return min(n, 1)
    return trib(n - 1) + trib(n - 2) + trib(n - 3)

class Solution:
    def tribonacci(self, n: int) -> int:
        return trib(n)
