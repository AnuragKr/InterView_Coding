ENDS_HERE = '#'

class Trie:
    
    def __init__(self):
        self._trie = {}

    def insert(self,text):
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[ENDS_HERE] = True
    
    def find(self,prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        return self._elements(trie)
    
    def _elements(self,d):
        result = []
        for c,v in d.items():
            if c == ENDS_HERE:
                subresult = ['']
            else:
                subresult = [c + s for s in self._elements(v)]
            result.extend(subresult)
        return result
    
    def autocomplete(self,s):
        suffixes = self.find(s)
        return [s + w for w in suffixes]

if __name__ == "__main__":
    trie = Trie()
    WORDS = ['dog','deer','deal']
    for word in WORDS:
        trie.insert(word)
    print(trie.autocomplete('d'))
    