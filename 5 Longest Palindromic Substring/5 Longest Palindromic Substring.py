"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1 or s == s[::-1]:
            return s
        maxlen = 1
        maxStart = 0
        for i in range(1, len(s)):
            start = i - maxlen - 1
            odd = s[start : i + 1]
            if start >= 0 and odd == odd[::-1]:
                maxStart = start
                maxlen += 2
            else:
                start = i - maxlen
                even = s[start : i + 1]
                if start >= 0 and even == even[::-1]:
                    maxStart = start
                    maxlen += 1
        return s[maxStart: maxStart + maxlen]
