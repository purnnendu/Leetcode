"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int)
        d[0] = 1 #for first subarray k-0=k
        tmp_sum = 0;res = 0
        for i in range(len(nums)):
            tmp_sum += nums[i]
            if tmp_sum - k in d:
                res += d[tmp_sum - k]
            d[tmp_sum] += 1
        return res
