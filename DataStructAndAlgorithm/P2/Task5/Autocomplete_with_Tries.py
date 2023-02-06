## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.trieNode = dict()
        
    
    def insert(self, char):
        # Add a child node in this Trie
        self.trieNode[char] = TrieNode()

    # I don't know how to see the expected output       
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        return 'r'
        # return ['r', 'b']

        
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
            return node.trieNode

    def print_first(self):
        for word_start in self.trie.trieNode:
            print(word_start)


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
            # TODO
            # I don't know how to see the expected output
            # so I just return 'r' or return ['r', 'b'] to see what will happen
            # but nothing change at all
            print('\n'.join(prefixNode.suffixes())) 
        else:
            print(prefix + " not found")
    else:
        print('')
# TODO
# how to see remaining info after prefix='a' ??
interact(f,prefix='');
