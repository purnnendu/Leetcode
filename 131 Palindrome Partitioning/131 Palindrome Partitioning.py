"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = collections.defaultdict(list)
        return self.partition_recursive(s, 0, memo)

    def partition_recursive(self, s, start, memo):
        s_len = len(s)
        if start == s_len:
            return [[]]
        if start in memo:
            return memo[start]
        for i in range(start, s_len):
            prefix = s[start: i+1]
            if not self.is_palindrome(prefix):
                continue
            partition_list = self.partition_recursive(s, i+1, memo)
            memo[start].extend([[prefix] + partition for partition in partition_list])
        return memo[start]

    def partition_iterative_dp(self, s: str) -> List[List[str]]:
        s_len = len(s)
        dp = [[False] * (s_len+1) for _ in range((s_len+1))]
        dp[0][0] = True
        res = [[] for _ in range(s_len+1)]
        res[0] = [[]]
        for end in range(1, s_len+1):
            for start in range(1, end+1):
                if not (start == end or start + 1 == end or dp[start+1][end-1]):
                    continue
                if s[start-1] != s[end-1]:
                    continue
                dp[start][end] = True
                for palindrome in res[start-1]:
                    res[end].append(palindrome + [s[start-1: end]])
        return res[s_len]

    def partition2(self, s: str) -> List[List[str]]:
        s_len = len(s)
        dp = [[] for _ in range(s_len)]
        dp[0].append([s[0]])
        for i in range(1, s_len):
            visited = set()
            for partition in dp[i-1]:
                for k in range(len(partition)+1):
                    new_str = ''.join(partition[k:]) + s[i]
                    new_partition = partition[:k] + [new_str]
                    if ' '.join(new_partition) in visited:
                        continue
                    if not self.is_palindrome(new_str):
                        continue
                    dp[i].append(new_partition)
                    visited.add(' '.join(new_partition))
        return dp[s_len-1]

    def is_palindrome(self, string):
        start, end = 0, len(string)-1
        while start <= end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
