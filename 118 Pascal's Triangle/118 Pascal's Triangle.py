"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cur=[1]
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        output=[[1],[1,1]]
        cur=[1,1]
        for row in range(3,numRows+1):
            temp=[1]
            for i in range(row-1):
                if i==row-2:
                    temp.append(1)
                else:
                    temp.append(cur[i]+cur[i+1])
            output.append(temp)
            cur=temp
        return output
