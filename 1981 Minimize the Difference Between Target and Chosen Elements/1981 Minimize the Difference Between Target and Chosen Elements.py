"""
You are given an m x n integer matrix mat and an integer target.
Choose one integer from each row in the matrix such that the absolute difference between target and the sum of the chosen elements is minimized.
Return the minimum absolute difference.
The absolute difference between two numbers a and b is the absolute value of a - b.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
Output: 0
Explanation: One possible choice is to:
- Choose 1 from the first row.
- Choose 5 from the second row.
- Choose 7 from the third row.
The sum of the chosen elements is 13, which equals the target, so the absolute difference is 0.

Example 2:

Input: mat = [[1],[2],[3]], target = 100
Output: 94
Explanation: The best possible choice is to:
- Choose 1 from the first row.
- Choose 2 from the second row.
- Choose 3 from the third row.
The sum of the chosen elements is 6, and the absolute difference is 94.

Example 3:

Input: mat = [[1,2,9,8,7]], target = 6
Output: 1
Explanation: The best choice is to choose 7 from the first row.
The absolute difference is 1.
"""
class Solution:
    def minimizeTheDifference(self, a: List[List[int]], t: int) -> int:
        def f(i,x,d):
            if x-sm[i]>=0:
                return x-sm[i]
            if x-sn[i]<=0 or i==n:
                return abs(x-sn[i])
            if (i,x) not in d:
                z=1<<32
                for j in range(m):
                    z=min(z,f(i+1,x-a[i][j],d))
                    if z==0:
                        break
                d[i,x]=z
            return d[i,x]
        n=len(a)
        m=len(a[0])
        sn=[0]*(n+1)
        sm=[0]*(n+1)
        for i in range(n-1,-1,-1):
            sn[i]=sn[i+1]+min(a[i])
            sm[i]=sm[i+1]+max(a[i])
        return f(0,t,{})
