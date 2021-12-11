"""
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0     ###// No prime number less than 2
        lst = [1] * n          ###// create a list for marking numbers less than n
        lst[0] = lst[1] = 0    ###// 0 and 1 are not prime numbers
        m = 2
        while m * m < n:       ###// we only check a number (m) if its square is less than n
            if lst[m] == 1:    ###// if m is already marked by 0, no need to check its multiples.

			    ###// If m is marked by 1, we mark all its multiples from m * m to n by 0.
			    ###// 1 + (n - m * m - 1) // m is equal to the number of multiples of m from m * m to n
                lst[m * m: n: m] = [0] *(1 + (n - m * m - 1) // m)

			###// If it is the first iteration (e.g. m = 2), add 1 to m (e.g. m = m + 1;
			### // which means m will be 3 in the next iteration),
            ###// otherwise: (m = m + 2); This way we avoid checking even numbers again.
            m += 1 if m == 2 else 2
        return sum(lst)
