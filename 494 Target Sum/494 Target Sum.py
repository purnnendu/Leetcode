"""
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1
"""
def branch(arr,start):
    counter = Counter( {start:1} )
    for x in arr:
        new = Counter()
        for k,v in counter.items():
            new[ k + x ] += v
            new[ k - x ] += v
        counter = new
    return counter
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        mid = len(nums)//2
        a,b = branch(nums[:mid],0), branch(nums[mid:][::-1],S)
        return sum([ a[x]*b[x] for x in set(a).intersection(set(b)) ])
    
