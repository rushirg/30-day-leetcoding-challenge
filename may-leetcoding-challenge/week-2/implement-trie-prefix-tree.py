"""
Week 2 - Problem 7
Implement Trie (Prefix Tree)
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3329/
"""


class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        myRoot = self.root
        length = len(word)
        for i in range(length):
            index = self.charToIndex(word[i])

            if not myRoot.children[index]:
                myRoot.children[index] = self.getNode()
            myRoot = myRoot.children[index]
        myRoot.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        myRoot = self.root
        length = len(word)
        for i in range(length):
            index = self.charToIndex(word[i])
            if not myRoot.children[index]:
                return False
            myRoot = myRoot.children[index]
        return myRoot != None and myRoot.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        myRoot = self.root
        length = len(prefix)
        for i in range(length):
            index = self.charToIndex(prefix[i])
            if not myRoot.children[index]:
                return False
            myRoot = myRoot.children[index]
        return myRoot != None



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)