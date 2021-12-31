"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        target = [0 for _ in range(26)]
        window = [0 for _ in range(26)]

        for i in range(n1):
            target[ord(s1[i]) - 97] += 1
            window[ord(s2[i]) - 97] += 1

        if(target == window):
            return True

        for i in range(n1, n2):
            window[ord(s2[i - n1]) - 97] -= 1
            window[ord(s2[i]) - 97] += 1

            if target == window:
                return True

        return False
