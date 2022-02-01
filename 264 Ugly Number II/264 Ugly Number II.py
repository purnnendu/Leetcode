"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""
from heapq import *

h=[1]
heapify(h)
n=1
ans=[]
s=set([1])

while(n!=1691):
    x=heappop(h)
    ans.append(x)
    if 2*x not in s:
        s.add(2*x)
        heappush(h,2*x)
    if 3*x not in s:
        s.add(3*x)
        heappush(h,3*x)
    if 5*x not in s:
        s.add(5*x)
        heappush(h,5*x)
    n+=1

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return ans[n-1]
