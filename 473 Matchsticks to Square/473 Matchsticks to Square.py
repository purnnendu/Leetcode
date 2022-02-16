"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.

Example 1:

Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
"""
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # backtracking
        s = sum(matchsticks)
        n = len(matchsticks)
        if s % 4 != 0:
            return False
        target = s // 4
        matchsticks.sort(reverse=True)
        # @lru_cache(None)
        def dfs(a, b, c, d, i):
            if i == n:

                return True
                # if a == target and b == target and c == target:
                #     return True
                # else:
                #     return False
            if a + matchsticks[i] <= target and dfs(a + matchsticks[i], b, c, d, i + 1):
                    return True
            if b != a and b + matchsticks[i] <= target and dfs(a, matchsticks[i]+ b, c, d, i + 1):
                    return True
            if b != c and c + matchsticks[i] <= target and dfs(a,  b, c + matchsticks[i], d, i + 1):
                return True
            if c != d and d + matchsticks[i] <= target and dfs(a,  b, c, d + matchsticks[i], i + 1):
                return True
            return False

        return dfs(0,0,0,0,0)
