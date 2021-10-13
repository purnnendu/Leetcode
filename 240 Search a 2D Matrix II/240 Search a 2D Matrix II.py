"""
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example 1:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:

Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.found = False
        def binary_search(arr, left, right,val):

            # print(arr, left, right, val)
            if left <= right:
                pivot_index = (left+right)//2
                pivot = arr[pivot_index]
                # print("pivot_index:", pivot_index, ", pivot:", pivot)
                if pivot == val:
                    self.found = True
                    # print("Found")
                    return
                if pivot < val:
                    #move right
                    binary_search(arr, pivot_index+1, right, val)
                else:
                    binary_search(arr, left, pivot_index-1, val)
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            binary_search(matrix[i], 0, n-1, target)
            # print("here", found)
            if self.found:  return True
            self.found = False
        return False
