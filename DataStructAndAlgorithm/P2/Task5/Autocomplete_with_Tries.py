## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.trieNode = dict()
    
    def insert(self, char):
        # Add a child node in this Trie
        self.trieNode[char] = TrieNode()
      
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffix_list = []
        for values in self.trieNode:
            if self.trieNode[values].trieNode:
                suffix_list.extend(self.trieNode[values].suffixes(suffix + values))
            else:
                suffix_list.append(suffix + values)
                
        return suffix_list
                    
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.trie = TrieNode()

    def insert(self, word):
        
        ## Add a word to the Trie
        trie = self.trie
        for char in word:
            if char not in trie.trieNode:
                trie.insert(char)

            trie = trie.trieNode[char]

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if prefix in self.trie.trieNode:
            node = self.trie.trieNode[prefix]
            return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes())) 
        else:
            print(prefix + " not found")
    else:
        print('')

interact(f,prefix='f');
