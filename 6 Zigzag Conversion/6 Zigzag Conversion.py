"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # dp = [[0 for _ in range(3)] for _ in range(len(costs))]
        r = [''] * numRows

        curRows = 0
        up = 0
        for c in s:
            if 0 < curRows < numRows - 1:
                if up == 0:
                    r[curRows] += c
                    curRows += 1
                else:
                    r[curRows] += c
                    curRows -= 1
            elif curRows == numRows - 1:
                r[curRows] += c
                curRows -= 1
                up = 1
            else:
                r[curRows] += c
                curRows += 1
                up = 0

        return ''.join(r)
