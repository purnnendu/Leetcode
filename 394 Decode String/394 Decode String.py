"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""
# Solution 1 memory efficient than 2

class Solution:
    def decodeString(self, s: str) -> str:
        out = ""
        replace = {"[":"(", "]":")"}
        for i in range(len(s)):
            if s[i].isdigit():
                out += '+' + s[i] if not s[i-1].isdigit() else s[i]
                if not s[i+1].isdigit():
                    out += '*'
            elif s[i].isalpha():
                out += "'" + s[i] + "'" if s[i-1]=='[' else "+'" + s[i] + "'"
            else:
                out += replace[s[i]]
        return eval(out.lstrip('+')) if s else s

# Solution 2

import re

class Solution:
    def decodeString(self, s: str) -> str:

        while True:
			# find a match with a number followed by a bracket enclosing a substring (with no more brackets inside)
            match = re.search('(\d+)\[(\w+)\]', s)

			# if no match we are done
            if not match:
                break

			# break the match into the number and substring
            mult = int(match.group(1))
            sub = match.group(2)

			# substitute the original match with the substring multiplied by the number and continue with the updated string
            s = re.sub('\d+\[\w+\]', mult*sub, s, 1)

        return s
