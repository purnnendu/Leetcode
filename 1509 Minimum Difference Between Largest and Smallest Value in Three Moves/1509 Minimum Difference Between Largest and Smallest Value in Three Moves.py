"""
You are given an integer array nums. In one move, you can choose one element of nums and change it by any value.
Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

Example 1:

Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.

Example 2:

Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1].
The difference between the maximum and minimum is 1-0 = 1.

"""
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        edges = heapq.nsmallest(4, nums) + list(reversed(heapq.nlargest(4, nums)))
        l = 0
        r = len(edges) - 1
        return min(edges[r-3+i] - edges[l+i] for i in range(4))
