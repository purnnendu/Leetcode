"""
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

    0, 1, and 8 rotate to themselves,
    2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
    6 and 9 rotate to each other, and
    the rest of the numbers do not rotate to any other number and become invalid.

Given an integer n, return the number of good integers in the range [1, n].

Example 1:

Input: n = 10
Output: 4
Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Example 2:

Input: n = 1
Output: 0

Example 3:

Input: n = 2
Output: 1
"""
class Solution:
    def rotatedDigits(self, N: int) -> int:  # O(logn)
        s1, s2 = set([0, 1, 8]), set([0, 1, 8, 2, 5, 6, 9])
        res, s = 0, set()
        N = list(map(int, str(N)))  # 157 -> [1, 5, 7]
        for i, v in enumerate(N):
            for j in range(v):
                if s.issubset(s2) and j in s2: # there are n-i-1 digits remain
                    res += 7**(len(N) - i - 1)  # combinations of s2
                if s.issubset(s1) and j in s1:
                    res -= 3**(len(N) - i - 1)  # combinations of s1, same number, so discount
            if v not in s2: return res  # if it's 3, 4, 7, then we can't do it after this number
            s.add(v)
        return res + (s.issubset(s2) and not s.issubset(s1))
