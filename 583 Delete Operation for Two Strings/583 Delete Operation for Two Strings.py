"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        bigw, smw = (word1, word2) if len(word1) >= len(word2) else (word2, word1)
        chpos = defaultdict(list)
        for i, ch in enumerate(smw):
            chpos[ch].append(i)

        len_upto_idx = [0] * (len(smw) + 1)
        for ch in bigw:
            if ch not in chpos: continue
            agg = list(accumulate(len_upto_idx[:chpos[ch][-1]+1], max))
            for i in reversed(chpos[ch]):
                len_upto_idx[i+1] = agg[i] + 1

        maxcommon = max(len_upto_idx[1:])
        return len(bigw) + len(smw) - 2 * maxcommon
