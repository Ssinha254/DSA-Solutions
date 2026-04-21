# Last updated: 4/21/2026, 11:26:11 PM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node,index):
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch != '.':
                if ch  in node.children:
                    return dfs(node.children[ch], index + 1)
                return False
            else:
                for child in node.children:
                    if dfs(node.children[child], index+ 1):
                        return True
                return False
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)