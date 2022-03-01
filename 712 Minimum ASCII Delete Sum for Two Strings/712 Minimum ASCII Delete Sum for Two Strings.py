"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1), len(s2)
        if m*n == 0:
            return 0
        last_row = [0]*(n+1)
        total = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        for i in range(m):
            cur_row = [0]*(n+1)
            for j in range(n):
                if s1[i] == s2[j]:
                    cur_row[j+1] = last_row[j] + ord(s1[i]) * 2
                else:
                    cur_row[j+1] = max(last_row[j+1],cur_row[j])
            last_row = cur_row
        return total-last_row[n]
