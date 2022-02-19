"""
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        chars = set()
        for c in s:
            chars.add(c)

        print(chars)

        @cache
        def lps(i, j):
            ss = s[i:j+1]
            res = 0
            for c in chars:
                if c not in ss:
                    continue
                ii = ss.index(c)
                jj = ss.rindex(c)
                res = max(res, lps(i+ii+1, i+jj-1)+2 if ii != jj else 1)
            return res

        return lps(0, len(s)-1)
