"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

    Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        for num in nums:
            points[num] = points.setdefault(num, 0) + num

        # assign nums to keys in sorted order
        nums = sorted(points.keys())
        cache = [0] * (len(nums) + 1)
        cache[1] = max(0, points[nums[0]])  # compare vals; gotta start loop at 2nd element

        for i in range(2, len(cache)):
            num = nums[i - 1]  # cache is one index ahead
            cache[i] = max(
                points[num] + (cache[i - 2] if nums[i - 2] == num - 1 else cache[i - 1]),  # take
                cache[i - 1]  # leave
            )
        return cache[-1]
