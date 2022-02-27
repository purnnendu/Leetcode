"""
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        piles, endOfPiles, cumulatedPaths = [], [], []
        for num in nums:
            pileIndex = bisect.bisect_left(endOfPiles, num)
            numOfPaths = 1
            if pileIndex > 0:
                prevIndex = bisect.bisect(piles[pileIndex-1], -num)
                numOfPaths = cumulatedPaths[pileIndex-1][-1] - cumulatedPaths[pileIndex-1][prevIndex]

            if len(piles) == pileIndex:
                piles.append([-num])
                endOfPiles.append(num)
                cumulatedPaths.append([0,numOfPaths])
            else:
                piles[pileIndex].append(-num)
                endOfPiles[pileIndex] = num
                cumulatedPaths[pileIndex].append(numOfPaths+cumulatedPaths[pileIndex][-1])
        return cumulatedPaths[-1][-1]
