"""
Week 1 - Problem 4
Reverse String
https://leetcode.com/problems/reverse-string/solution/
"""


# method 1
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stringLength = len(s)
        for i in range(stringLength//2):
            tmp = s[stringLength - i - 1]
            s[stringLength - i - 1] =  s[i]
            s[i] = tmp


# method 2
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s.reverse()


# method 3
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1