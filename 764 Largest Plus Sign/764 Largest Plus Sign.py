"""
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example 1:

Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

Example 2:

Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
"""
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: [[int]]) -> int:
        cols = [[-1,n] for _ in range(n)]
        rows = [[-1,n] for _ in range(n)]
        for r,c in mines:
            cols[c].append(r)
            rows[r].append(c)
        for i in range(n):
            cols[i].sort()
            rows[i].sort()
        res = 0
        for r in range(n):
            for i in range(len(rows[r])-1):
                left = rows[r][i]+1
                right = rows[r][i+1]-1
                for c in range(left+res, right-res+1):
                    idx = bisect.bisect_right(cols[c],r)
                    up = cols[c][idx-1]+1
                    down = cols[c][idx]-1
                    # print(r,c,left,right,up,down)
                    origRes = res
                    res = max(res, min(c-left+1,right-c+1,r-up+1, down-r+1))
        return res
