"""
You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""
import functools
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def countMN(st):
            n0 = 0
            m0 = 0
            for i in st:
                if i == '0':
                    m0+=1
                else:
                    n0+=1
            #val =  (m0/n) + (n0/m)
            return (m0,n0,  len(st), m0/m, n0/n)

        def findSol(arr):
            count = 0
            m0 = 0
            n0= 0
            for i in arr:
                if(m0 + i[0] > m or n0 + i[1] > n):
                    continue
                m0 += i[0]
                n0 += i[1]
                count+=1
            return count

        largest  = 0

        arr = [countMN(x) for x in strs]

        def compare(s1, s2):
            if(s1[3]==s2[3]):
                if(s1[2]<s2[2]):
                    return -1
                elif(s1[2]>s2[2]):
                    return 1
                else:
                    return 0
            else:
                if(s1[3]<s2[3]):
                    return -1
                elif(s1[3]>s2[3]):
                    return 1
                else:
                    return 0

        def compare1(s1, s2):
            if(s1[4]==s2[4]):
                if(s1[2]<s2[2]):
                    return -1
                elif(s1[2]>s2[2]):
                    return 1
                else:
                    return 0
            else:
                if(s1[4]<s2[4]):
                    return -1
                elif(s1[4]>s2[4]):
                    return 1
                else:
                    return 0

        def compare2(s1, s2):
            if(s1[2]==s2[2]):
                if(s1[0]<s2[0]):
                    return -1
                elif(s1[0]>s2[0]):
                    return 1
                else:
                    return 0
            else:
                if(s1[2]<s2[2]):
                    return -1
                elif(s1[2]>s2[2]):
                    return 1
                else:
                    return 0

        arr  = sorted(arr, key=functools.cmp_to_key(compare1))
        largest = max(largest, findSol(arr))

        arr = sorted(arr, key=functools.cmp_to_key(compare))
        largest = max(largest, findSol(arr))

        arr = sorted(arr, key=functools.cmp_to_key(compare2))
        largest = max(largest, findSol(arr))

        return largest
