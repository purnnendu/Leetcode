"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat[0][0] == 1:
            mat[0][0] = float('inf')

        for i in range(1, len(mat[0])):
            if mat[0][i] == 1:
                mat[0][i] = mat[0][i-1] + 1

        for i in range(1, len(mat)):
            if mat[i][0] == 1:
                mat[i][0] = mat[i-1][0] + 1

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                if mat[i][j] == 1:
                    mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + 1

        for i in range(len(mat[0])-2, -1, -1):
            if mat[-1][i] != 0:
                mat[-1][i] = min(mat[-1][i+1] + 1, mat[-1][i])

        for i in range(len(mat)-2, -1, -1):
            if mat[i][-1] != 0:
                mat[i][-1] = min(mat[i+1][-1] + 1, mat[i][-1])

        for i in range(len(mat)-2, -1, -1):
            for j in range(len(mat[0])-2, -1, -1):
                if mat[i][j] != 0:
                    mat[i][j] = min(min(mat[i+1][j], mat[i][j+1])+1, mat[i][j])
        return mat
