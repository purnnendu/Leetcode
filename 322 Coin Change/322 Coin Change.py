"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2
"""
class Solution:
    def coinChange(self, coins: List[int], target: int) -> int:
        if target == 0:
            return 0

        mask = 1 << target
        count = 0
        while mask & 1 != 1:
            new_mask = mask
            for coin in coins:
                new_mask |= mask >> coin
            if mask == new_mask:
                # cannot reach any new state, reaching 0 is impossible
                return -1
            mask = new_mask
            count += 1

        return count
