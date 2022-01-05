"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
"""
class Solution(object):
    def letterCasePermutation(self, s: str) -> List[str]:

        def recursion(s):
            if(len(s)==0):
                return [""]
            lastElem=s[-1]
            array=recursion(s[:-1])

            intValue=ord(lastElem)
            second=0

            if(65<=intValue<=90):
                second=chr(97+intValue-65)

            if(97<=intValue<=122):
                # first=lastElem
                second=chr(65+intValue-97)

            length=len(array)
            for num,let in enumerate(array):
                new=let
                new+=lastElem
                array[num]=new
                if(second!=0):
                    new2=let
                    new2+=second
                    array.append(new2)

                if(num==length-1):
                    break

            return array
        return recursion(s)
