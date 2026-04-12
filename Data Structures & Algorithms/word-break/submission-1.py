class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)

        dp = {}

        def dfs(i):
            if i >= len(s):
                return True

            if i in dp:
                return dp[i]

            dp[i] = False
            for word in wordDict:
                n = len(word)
                if s[i:i+n] == word:
                    dp[i] = dfs(i+n)
                    if dp[i]:
                        return dp[i]

            return dp[i]

        return dfs(0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, string):
        cur = self.root
        for c in string:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def prefix(self, string):
        cur = self.root
        for c in string:
            print(cur.children)
            if c not in cur.children:
               return False
            cur = cur.children[c] 
        return True

    def find(self, string):
        cur = self.root
        for c in string:
            if c not in cur.children:
               return False
            cur = cur.children[c]
        return cur.word