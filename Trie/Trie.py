class Trie:

    def __init__(self):
        self.childs = [None] * 26 # English Words
        self.is_leaf = False

    def _to_idx(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word, idx = 0):
        if idx == len(word):
            self.is_leaf = True
        else:
            cursur = self._to_idx(word[idx])
            if self.childs[cursur] is None:
                self.childs[cursur] = Trie()
            self.childs[cursur].insert(word, idx+1)

    def find(self, word, idx = 0):
        if idx == len(word):
            return self.is_leaf
        
        cursur = self._to_idx(word[idx])
    
        if self.childs[cursur] is None:
            return False
        
        return self.childs[cursur].find(word, idx+1)
    
    def find_prefix(self, word, idx = 0):
        if idx == len(word)-1:
            return True
        
        cursur = self._to_idx(word[idx])
    
        if self.childs[cursur] is None:
            return False
        
        return self.childs[cursur].find_prefix(word, idx+1)
    

    def first_word_prefix(self, word, idx = 0):
        cur = self._to_idx(word[idx])
        
        if self.childs[cur] is None or self.is_leaf:
            return ''
        

        
        return word[idx] + self.childs[cur].first_word_prefix(word, idx+1)
    
    def show(self, str = ''):

        words = []

        def travers(current, word = ''):

            if current.is_leaf:
                words.append(word)

            for idx, node in enumerate(current.childs):
                if node is None:
                    continue
                letter = chr(ord('a') + idx)
                travers(node, word + letter)


        travers(self, str)

        return words
    
    def autocomplete(self, prefix):
        
        node = self

        for chr in prefix:
            if node is None:
                return []
            cur = self._to_idx(chr)
            node = node.childs[cur]
        return node.show(prefix)

    def majic_search(self, target):
        
        def process(current, target, idx):
            if idx == len(target):
                return 1
            
            

            


        thesame = process(self, target, idx = 0)

        if thesame == len(target) -1:
            return True
        else:
            return False










trie = Trie()
trie.insert("ab")
trie.insert("afdfdf")
trie.insert("afdfsdfsa")
trie.insert("ahhtggf")
trie.insert("gdfrthhth")
print(trie.autocomplete('g'))

