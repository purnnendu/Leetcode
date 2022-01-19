"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = set(), len(nums)

        nums.sort()
        numDict = {num: i for i, num in enumerate(nums)}

        i = bisect_left(nums, target - sum(nums[-3:]), 0, n)  # lowest bound for target
        r1 = bisect_right(nums, target / 4, i, n)  # upper bound for target
        while i < r1:
            target2 = target - nums[i]
            j = bisect_left(nums, target2 - sum(nums[-2:]), i + 1, n)
            r2 = bisect_right(nums, target2 / 3, j, n)
            while j < r2:
                end3 = bisect_right(nums, target2 - nums[j] * 2, j + 1, n)
                target3 = target2 - nums[j]
                k = bisect_left(nums, target3 - nums[end3-1], j + 1, end3)
                r3 = bisect_right(nums, target3 / 2, k, n)
                while k < r3:
                    target4 = target3 - nums[k]
                    if (target4 in numDict) and (numDict[target4] > k):
                        res.add((nums[i], nums[j], nums[k], target4))
                    k = numDict[nums[k]] + 1
                j = numDict[nums[j]] + 1
            i = numDict[nums[i]] + 1

        return res
