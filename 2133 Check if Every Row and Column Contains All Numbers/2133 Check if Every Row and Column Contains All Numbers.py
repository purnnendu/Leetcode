"""
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

Example 1:

Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

Example 2:

Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.
"""
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for item in matrix:
            if sorted(item) != [i for i in range(1, len(item) + 1)]:
                return False
        for item in list(map(list, zip(*matrix))):
            if sorted(item) != [i for i in range(1, len(item) + 1)]:
                return False
        return True
