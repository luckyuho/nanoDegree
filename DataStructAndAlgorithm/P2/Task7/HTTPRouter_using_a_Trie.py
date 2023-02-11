# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.routeTrie = RouteTrieNode()

    def insert(self, words, http_handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.routeTrie

        for word in words:
            if word not in node.routeTrieNode:
                node.insert(word)
            node = node.routeTrieNode[word]
            
        node.is_handler = True
        node.http_handler = http_handler

    def find(self, words, root_handler="root handler", not_found_handler="not_found_handler"):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if len(words) < 1:
            return root_handler

        node = self.routeTrie

        for word in words:
            if word not in node.routeTrieNode:
                return not_found_handler
            node = node.routeTrieNode[word]

        if not node.http_handler:
            return not_found_handler
            
        return node.http_handler
        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.routeTrieNode = dict()
        self.is_handler = False
        self.http_handler = None

    def insert(self, word):
        # Insert the node as before
        self.routeTrieNode[word] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        self.routeTrie = RouteTrie()

    def add_handler(self, http_path, http_handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        word_arr = self.split_path(http_path)

        self.routeTrie.insert(word_arr, http_handler)

    def lookup(self, http_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        words = self.split_path(http_path)
        return self.routeTrie.find(words, self.root_handler, self.not_found_handler)

    def split_path(self, words):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        all_arr = words.split("/")
        word_arr = []

        for word in all_arr:
            if word != '':
                word_arr.append(word)
        return word_arr

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/experience", "about experience handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Test Edge Cases
print(router.lookup("/home/experience")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/experience")) # should print 'not found handler' or None if you did not implement one
