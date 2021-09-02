"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        lower = self.generateParenthesis(n-1)
        output = []
        for elem in lower:
            for i in range(len(elem)):
                output.append(elem[:i] + "()" + elem[i:])
        return list(set(output))
