"""
In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers.
For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.

Example 1:

Input: maxChoosableInteger = 10, desiredTotal = 11
Output: false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

Example 2:

Input: maxChoosableInteger = 10, desiredTotal = 0
Output: true

Example 3:

Input: maxChoosableInteger = 10, desiredTotal = 1
Output: true
"""
import functools
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger >= desiredTotal:
            return True
        if maxChoosableInteger*(maxChoosableInteger+1)/2 < desiredTotal:
            return False

        def dfs(maxChoosableInteger, curDesiredTotal, cache, key):
            if curDesiredTotal <= maxChoosableInteger:
                return True
            if key in cache:
                return cache[key]

            for i in range(1, maxChoosableInteger):
                if key & 1 << i:
                    continue
                key |= 1 << i
                if not dfs(maxChoosableInteger, curDesiredTotal - i, cache, key):
                    cache[key ^ 1 << i] = True
                    return True
                key ^= 1 << i
            cache[key] = False
            return False


        return dfs(maxChoosableInteger, desiredTotal, {}, 0)
