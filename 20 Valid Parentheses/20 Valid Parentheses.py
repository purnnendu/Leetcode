"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

"""
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(':')',
            '[':']',
            '{':'}'
        }
        expected_close = []
        for e in s:
            # found an opening parenthesis
            if e in pairs:
                expected_close.append(pairs[e])
            # is closing parenthises
            else:
                if expected_close == [] or expected_close.pop() != e:
                    return False
        if len(expected_close) > 0:
            return False
        return True
