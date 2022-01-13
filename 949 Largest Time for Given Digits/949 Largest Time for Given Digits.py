"""
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:

Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
"""
from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
    	T, M = [], 0
    	for t in set(permutations(A)):
    		h = t[0]*10 + t[1]
    		m = 60*h + 10*t[2] + t[3]
    		if h <= 23 and t[2] in [0,1,2,3,4,5] and m < 1440 and m > M: M, T = m, t
    	return f"{T[0]}{T[1]}:{T[2]}{T[3]}" if len(T) !=0 else "00:00" if A == [0,0,0,0] else ""
