
class TrieNode: 
    def __init__(self): 
        self.children = {} # 26 characters max. 
        # T.children = {["a", TN1], ["b", TN2], ...} 
        self.eow = False # endOfWord

class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self, word: str) -> None:
        # iterate through list of characters in the word and add them to 
        # the trie if they already don't exist. 
        cur = self.root 

        for c in word: 
            # char not a child of the trie Nod, 
            if c not in cur.children: 
                cur.children[c] = TrieNode() # add the character to the trie 
            cur = cur.children[c]
        # we are at the end of the word, so we set node.eow to true. 
        cur.eow = True 

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word: 
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.eow    

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 

        for c in prefix: 
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
