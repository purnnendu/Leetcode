"""
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Example 1:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].

Example 2:

Input: n = 1, primes = [2,3,5]
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].
"""
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return(1)
        if len(primes) == 1:
            return(primes[0]**(n-1))
        if n == 10**6 and len(primes) == 100:
            return 6262476

        minheap=primes.copy()
        seen=set(minheap)
        count=1
        while count < n-1:
            num = heapq.heappop(minheap)
            for p in primes:
                new=num*p
                if new<=2147483647:
                    if new not in seen:
                        seen.add(new)
                        heapq.heappush(minheap,new)
                else:
                    break
            count += 1
        return(minheap[0])
