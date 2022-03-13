"""
You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

Example 1:

Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
"""
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        len_mountain = slope = 0
        start = -1
        arr.append(arr[-1])    # to trigger len_mountain check in the loop
        for i, (a, b) in enumerate(zip(arr, arr[1:])):
            if b > a:
                if slope < 1:
                    if slope == -1 and start > -1:
                        len_mountain = max(len_mountain, i + 1 - start)
                    start = i
                    slope = 1
            elif b < a:
                if slope == 1:
                    slope = -1
            else:
                if slope == -1:
                    if start > -1:
                        len_mountain = max(len_mountain, i + 1 - start)
                slope = 0
                start = -1
        return len_mountain
