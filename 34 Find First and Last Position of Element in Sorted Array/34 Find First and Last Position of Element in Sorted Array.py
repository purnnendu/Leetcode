"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = - (- (left + right) // 2)
            if target >= nums[mid]:
                left = mid
            else:
                right = mid - 1
        if nums[left] == target:
            upper = left
        else:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        lower = left
        return [lower, upper]
