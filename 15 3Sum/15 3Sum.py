"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        counter = collections.defaultdict(int)
        for i in nums:
            counter[i] += 1
        # print(counter) -- defaultdict(<class 'int'>, {-1: 2, 0: 1, 1: 1, 2: 1, -4: 1})

        nums = sorted(counter)
        if nums[0]>0 or nums[-1]<0:
            return []
        

        output = []
        # find answer with no duplicates within combo
        for i in range(len(nums)):
            # search range
            twoSum = -nums[i]
            min_half, max_half = twoSum - nums[-1]  , twoSum/2
            l = bisect_left(nums, min_half, i+1)
            r = bisect_left(nums, max_half, l)

            for j in nums[l:r]:
                if twoSum - j in counter:
                    output.append([nums[i], j, twoSum-j])

        # find ans with duplicates within combo
        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0,0,0])
                elif k != 0 and -2*k in counter:
                    output.append([k, k, -2*k])
        return output
