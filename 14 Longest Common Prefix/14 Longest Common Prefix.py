"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length=201
        for i in range(len(strs)):
            if strs[i]=="":
                return ""
            if len(strs[i])<length:
                minindex=i
                length=len(strs[i])
        candidate=strs.pop(minindex)
        for i in range(len(candidate),0,-1):
            found=True
            candidate=candidate[:i]
            for j in range(0,len(strs)):
                if strs[j][:i]!=candidate:
                    found=False
                    break
            if found:
                return candidate
        if not found:
            return ""
