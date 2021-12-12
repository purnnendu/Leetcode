"""
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5
"""
class Solution:
    def calculate(self, s: str) -> int:
        s1 = s.replace('-', '+-').replace('/', '*1/')
        nums = s1.split('+')
        total = 0
        for num in nums:
            if '*' not in num:
                total += int(num)
            else:
                mull_nums = num.split('*')
                ini = 1
                for m in mull_nums:
                    if '/' not in m:
                        ini *= int(m)
                    else:
                        temp = m.split('/')
                        ini = int(ini/int(temp[1]))
                total += int(ini)
        return total

# Alternate one with better space complexity & speed

class Solution:
    def calculate(self, s: str) -> int:
        num, presign, stack=0, "+", []
        for i in s+'+':
            if i.isdigit():
                num = num*10 +int(i)
            elif i in '+-*/':
                if presign =='+':
                    stack.append(num)
                if presign =='-':
                    stack.append(-num)
                if presign =='*':
                    stack.append(stack.pop()*num)
                if presign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                presign = i
                num = 0
        return sum(stack)
