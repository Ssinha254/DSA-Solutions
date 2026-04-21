# Last updated: 4/21/2026, 11:26:57 PM
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        q = deque()
        q.append([beginWord, 1])
        s = set(wordList)
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            for i in range(len(word)):
                for j in range(ord('a'), ord('z') + 1):
                    newWord = word[:i] + chr(j) + word[i+1:]
                    if newWord in s:
                        q.append([newWord, level + 1])
                        s.remove(newWord)
        return 0
        
