"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution:

    def longestSubstring(self, s: str, k: int) -> int:
        return self.longestSubstringUtil(s, 0, len(s), k)

    def longestSubstringUtil(self, s, start, end, k):
        # print("markers", start, end)
        n = end-start

        if n == 0 or n < k:
            return 0
        if k <= 1:
            return n

        counts = defaultdict(int)
        for i in range(start, end):
            counts[s[i]] += 1
        # print(counts)

        idx = start
        while idx < end and counts[s[idx]] >= k:
            idx += 1
        if idx >= end-1:
            # Either full string [start:end] has chars with count >= k, or only last char count < k
            # print("return len", idx-start)
            return idx-start


        ls1 = self.longestSubstringUtil(s, start, idx, k)

        while idx < end and counts[s[idx]] < k:
            idx += 1
        ls2 = 0 if idx == end else self.longestSubstringUtil(s, idx, end, k)

        # print(ls1, ls2)
        # print("return len",  max(ls1, ls2))
        return max(ls1, ls2)
