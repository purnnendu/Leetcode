"""
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
"""
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = ''.join([chr(x) for x in nums2])
        max_str = ''
        res = 0
        for num in nums1:
            max_str+=chr(num)
            if max_str in nums2_str:
                res = max(res,len(max_str))
            else:
                max_str = max_str[1:]

        return res
