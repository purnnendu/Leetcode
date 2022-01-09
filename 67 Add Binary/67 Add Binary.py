"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))
        new_str = ''
        digit = 0

        if len(a)<len(b):
            strs = (a,b)
        else:
            strs = (b,a)
        short = len(strs[0])
        long = len(strs[1])


        for i in range(long):
            if i<short:
                sm = digit + int(strs[0][-i-1])+int(strs[1][-i-1])
            else:
                sm = digit +int(strs[1][-i-1]) # keep adding digits from longer string
            print(i,int(strs[1][-i]))

            if sm<=1:
                new_str = str(sm)+new_str
                digit=0
            if sm>=2:
                new_str = str(sm%2)+new_str
                digit=1

        if digit==1:
            new_str = '1'+new_str
        return new_str
