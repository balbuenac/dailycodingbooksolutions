from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for w in word:
            if not w in curr:
                curr[w] = {}
            curr = curr[w]
        curr["#"] = {}

    def search(self, word: str) -> bool:
        def helper(root, word):
            if not root:
                return

            if "#" in root and len(word) == 0:
                return True

            if len(word) == 0:
                return

            if word[0] == '.':
                res = False
                for v in root.values():
                    res = res or helper(v, word[1:])
                return res

            if not word[0] in root:
                return False

            return helper(root[word[0]], word[1:])

        if len(self.trie == 0:
            return False
        return helper(self.trie, word)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# partial matching ?? total matching ??
# regex ... chars than can be replaced ??
# . wildcard to replace words !!
#
)
