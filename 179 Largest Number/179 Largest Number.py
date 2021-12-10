"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"

Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:

Input: nums = [1]
Output: "1"

Example 4:

Input: nums = [10]
Output: "10"
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_sorted = sorted(nums, key=lambda x: (str(x) * 10), reverse=True)
        result = ''.join([str(num) for num in nums_sorted])
        return result if result[0] != '0' else '0'
