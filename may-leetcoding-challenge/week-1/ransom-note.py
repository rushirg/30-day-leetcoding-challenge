"""
Week 1 - Problem 3
Ransom Note
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if ransomNote == magazine or len(ransomNote) is 0:
            return True

        ransomDict = {}
        magazineDict = {}

        for ch in ransomNote:
            if ch in ransomDict:
                ransomDict[ch] += 1
            else:
                ransomDict[ch] = 1

        for ch in magazine:
            if ch in magazineDict:
                magazineDict[ch] += 1
            else:
                magazineDict[ch] = 1

        flag = True
        for key in ransomDict:
            if key in magazineDict:
                if magazineDict[key] < ransomDict[key]:
                    flag = False
            else:
                flag = False
        return False if flag is False else True

