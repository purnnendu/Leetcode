"""
You are given a string s.
A split is called good if you can split s into two non-empty strings sleft and sright where their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright is the same.
Return the number of good splits you can make in s.

Example 1:

Input: s = "aacaba"
Output: 2
Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.

Example 2:

Input: s = "abcd"
Output: 1
Explanation: Split the string as follows ("ab", "cd").
"""
class Solution:
    def numSplits(self, s: str) -> int:
        # this is not neccessary, but speeds things up
        length = len(s)
        if length == 1:  # never splittable
            return 0
        elif length == 2:  # always splittable
            return 1

		# we are recording the first and last occurance of each included letter
        first = {}  # max size = 26
        last = {}  # max size = 26

        for index, character in enumerate(s):  # O(n)
            if character not in first:
                first[character] = index
            last[character] = index

		# we are concatenating the collected indices into a list and sort them
        indices = list(first.values()) + list(last.values())  # max length 26 + 26 = 52
        indices.sort()  # sorting is constant O(1) because of the length limit above

		# all possible splits will be in the middle of this list
        middle = len(indices)//2  # always an integer because indices has an even length

		# there are this many possible splits between the two 'median' numbers
        return indices[middle] - indices[middle-1]
