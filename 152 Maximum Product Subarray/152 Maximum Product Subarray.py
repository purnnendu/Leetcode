"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        num = nums[0]
        if num > 0:
            best_positive = num
            best_negative = 0
        elif num < 0:
            best_positive = 0
            best_negative = num
        else:
            best_positive = 0
            best_negative = 0
        best = num
        n = len(nums)
        for i in range(1,n):
            num = nums[i]
            if num == 0:
                best_positive = 0
                best_negative = 0
            elif num < 0:
                p,n = best_positive, best_negative
                best_positive = n * num
                best_negative = min(p*num, num)
            else:
                p,n = best_positive, best_negative
                best_positive = max(p*num, num)
                best_negative = n*num
            if best_positive > best:
                best = best_positive
        return best
