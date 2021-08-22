"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # random string from 00..0 to 11..1 and check if the string is in array. If not, regenerate another random string
        import random
        n = len(nums)
        exists = set(nums)

        while True:
            val = random.randint(0, 2**n-1)
            mask = "{0:b}".format(val).zfill(n)
            if mask not in exists:
                return mask
