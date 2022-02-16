"""
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

    "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.

Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.

Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
"""

# dp[i] = the length of the longest conforming substrings ending at p[i]
# the key is the UNIQUE of the string
# for each substring, the ending char of the substring and the length uniquely determine the substring
# also, notice that for each index i in p, if there is a conforming substring ending at p[i] of length L, then there must also be substrings of length L-1, L-2, ...1.
# so for each p[i], the length of longest conforming substring is also the number of conforming substring.
# for each p[i], we maintain the length of the longest conforming substring
# also, we need to know the max length of conforming for each letter in A
# edge case: "cdefghefghi"

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        A = string.ascii_lowercase
        pre = {A[i]:A[i-1] for i in range(1,len(A))}
        pre['a'] = 'z'

        total = 1 # for p[0]
        ML = {c:0 for c in A} # max conforming length for each letter in A we've seen currently
        ML[p[0]] = 1 # we start for loop from p[1], so we need to manually tackle ML[p[0]]
        dp = [1] * len(p) # max conforming length for each index in p

        for i in range(1,len(p)):
            if pre[p[i]] == p[i-1]:
                dp[i] = 1 + dp[i-1]
            if dp[i] > ML[p[i]]:
                total += dp[i] - ML[p[i]]
                ML[p[i]] = dp[i]
        return total
