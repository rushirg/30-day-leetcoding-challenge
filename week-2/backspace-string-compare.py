"""
Week 2 - Problem 2
Backspace String Compare
https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3291/
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        def getBackspaceString(my_string):
            while True:
                if '#' in my_string:
                    index = my_string.index('#')
                    if index == 0:
                        my_string = my_string[index + 1:]
                    else:
                        my_string = my_string[:index - 1] + my_string[index + 1:]
                else:
                    break
            return my_string
        if getBackspaceString(S) == getBackspaceString(T):
            return True
        else:
            return False
