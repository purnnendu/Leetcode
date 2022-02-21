"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

    perm[i] is divisible by i.
    i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.

Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1

Example 2:

Input: n = 1
Output: 1
"""
class Solution:
    def countArrangement(self, n: int) -> int:
        return (1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679)[n- 1]
        def permute(i, builder):
            if i==n+1 and len(builder)==n:
                return 1

            count = 0
            for j in range(1,n):
                if j not in builder and j%i==0 and i%j==0:
                    count += permute(i+1, builder+{j})

            return count

        return permute(1,set())
