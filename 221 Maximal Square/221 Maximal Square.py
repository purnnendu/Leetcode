"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:

Input: matrix = [["0"]]
Output: 0
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        area = 0
        if matrix:
            prev = [0]*len(matrix[0])
            for row in matrix:
                s = [1 if ch == '1' else 0 for ch in row]
                for j in range(1,len(s)):
                    #if s[j] = 0 then still = 0 if not, we update
                    if s[j]:
                        s[j] = min(prev[j-1],prev[j],s[j-1])+1
                area = max(area,max(s)**2)
                prev = s
        return area
