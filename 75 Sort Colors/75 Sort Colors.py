"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:

Input: nums = [0]
Output: [0]

Example 4:

Input: nums = [1]
Output: [1]
"""
class Solution:
    def sortColors(self, N: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, R, i = 0, len(N) - 1, 0
        while i <= R:
            if N[i] == 0: N[L], N[i], L, i = 0, N[L], L + 1, i + 1
            elif N[i] == 2: N[R], N[i], R = 2, N[R], R - 1
            else: i += 1
