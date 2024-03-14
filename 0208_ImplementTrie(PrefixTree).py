class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            i = ord(w) - ord('a')

            if not curr.children[i]:
                curr.children[i] = TrieNode()  
            curr = curr.children[i]
        curr.end = True 
                    

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            i = ord(w) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr.end == True
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            i = ord(w) - ord('a')
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return True
  
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
