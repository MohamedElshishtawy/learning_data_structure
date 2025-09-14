class Trie:

    def __init__(self):
        self.childs = [None] * 26 # English Words
        self.is_leaf = False

    def _to_idx(self, char):
        return ord(char) - ord('a')
    
    def insert(self, word):
        
        def process(current, word, idx = 0):
            if idx == len(word):
                current.is_leaf = True
            else:
                cursur = current._to_idx(word[idx])
                if current.childs[cursur] is None:
                    current.childs[cursur] = Trie()
                process(current.childs[cursur], word, idx+1)

        word = word[::-1]
        process(self, word)

   
    
    def find_suffex(self, word):
        def process(current, word, idx = 0):
            if idx == len(word)-1:
                return True
            
            cursur = current._to_idx(word[idx])
        
            if current.childs[cursur] is None:
                return False
            
            return process(current.childs[cursur], word, idx+1)
        
        word = word[::-1]
        return process(self, word)




trie = Trie()
trie.insert("abcdef")
trie.insert("dffsfdfgdfvdvfdsdfvfsdg")
trie.insert("abcdfdgfdgfdsgfdsgef")
trie.insert("kjhkjytjhgj")
trie.insert("abcdflkhjgsgfsdgdfsgsdef")
trie.insert("jkkjllkjlk")
print(trie.find_suffex('gfsdgdfsgsdef'))

