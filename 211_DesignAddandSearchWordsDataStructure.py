class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self

        for w in word:
            i = ord(w) - ord('a')
            if not curr.children[i]:
                curr.children[i] = WordDictionary()
            curr = curr.children[i]
        curr.end = True
            
    def search(self, word: str) -> bool:
        curr = self

        for i in range(len(word)):
            w = word[i]

            if w == '.':
                for ch in curr.children:
                    if ch and ch.search(word[i+1:]):
                        return True
                return False

            i = ord(w) - ord('a')            
            if not curr.children[i]:
                return False
            curr = curr.children[i]
        return curr != None and curr.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
