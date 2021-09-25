"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""
class Solution:
    def wordBreak(self, s: str, A: List[str]) -> bool:
        A    = set(A)
        lens = sorted(map(len,A))
        #
        L = len(s)
        #
        memo = set()
        def dfs(i):
            # A) Previous Failed Attempt
            if i in memo:
                return False
            # B) Full Match (Triggers chained exits)
            if i==L:
                return True
            # C) Proper Search
            for x in lens:
                # 1) Length Exceeded
                if (x+i) > L:
                    break
                # 2) Find Match
                if s[i:i+x] in A and dfs(i+x):
                        return True
            # 3) Register Failed Attempt
            memo.add(i)
            return False
        return dfs(0)
