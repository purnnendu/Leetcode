"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(abs(numerator), abs(denominator))
        elif numerator < 0 or denominator < 0:
            return '-' + self.fractionToDecimal(abs(numerator), abs(denominator))
        div, mod = numerator // denominator, numerator % denominator
        curr = str(div)
        if mod == 0:
            return curr
        subZero = '.'
        mapping = {}
        while True:
            mod *= 10
            temp = mod
            div, mod = mod // denominator, mod % denominator
            if mod == 0:
                subZero += str(div)
                return curr + subZero
            if temp in mapping:
                repeatIndex = mapping[temp]
                return curr + subZero[:repeatIndex] + '(' + subZero[repeatIndex:] + ')'
            else:
                mapping[temp] = len(subZero)
                subZero += str(div)
