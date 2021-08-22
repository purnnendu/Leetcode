"""
You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).
Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.
An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.
Note: Test cases are generated such that there will always be at least one correct answer.

Example 1:

Input: n = 3, sums = [-3,-2,-1,0,0,1,2,3]
Output: [1,2,-3]
Explanation: [1,2,-3] is able to achieve the given subset sums:
- []: sum is 0
- [1]: sum is 1
- [2]: sum is 2
- [1,2]: sum is 3
- [-3]: sum is -3
- [1,-3]: sum is -2
- [2,-3]: sum is -1
- [1,2,-3]: sum is 0
Note that any permutation of [1,2,-3] and also any permutation of [-1,-2,3] will also be accepted.

Example 2:

Input: n = 2, sums = [0,0,0,0]
Output: [0,0]
Explanation: The only correct answer is [0,0].

Example 3:

Input: n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
Output: [0,-1,4,5]
Explanation: [0,-1,4,5] is able to achieve the given subset sums.
"""
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ans = []
        while len(sums) > 1:
            ele, sums = self._recoverArray(sums)
            ans.append(ele)
        return ans

    def _recoverArray(self, sums: List[int]) -> [int, List]:
        max_val = max(sums)
        L = len(sums)
        sums_map = {}
        for val in sums:
            if val not in sums_map:
                sums_map[val] = 0
            sums_map[val] += 1
        sorted_vals = sorted(sums_map.keys())
        init_low = sorted_vals[0]
        sums_map[init_low] -= 1
        if sums_map[init_low] == 0:
            del sums_map[init_low]
            sorted_vals.pop(0)
        for high in sorted_vals:
            _sums_map = sums_map.copy()
            _sums_map[high] -= 1
            if _sums_map[high] == 0:
                del _sums_map[high]
            count = 2
            diff = high - init_low
            ans = [init_low]
            for low in sorted_vals:
                skip_all_the_way = False
                while low in _sums_map:
                    _sums_map[low] -= 1
                    if _sums_map[low] == 0:
                        del _sums_map[low]
                    high = low + diff
                    if high not in _sums_map:
                        skip_all_the_way = True
                        break
                    _sums_map[high] -= 1
                    if _sums_map[high] == 0:
                        del _sums_map[high]
                    count += 2
                    ans.append(low)
                    if count == L:
                        skip_all_the_way = True
                        break
                if skip_all_the_way:
                    break
            if count == L:
                if 0 in set(ans):
                    return [diff, ans]
                return [-diff, [num + diff for num in ans]]
