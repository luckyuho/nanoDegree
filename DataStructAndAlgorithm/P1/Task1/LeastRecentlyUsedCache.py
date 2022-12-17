import time

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = [None for _ in range(capacity)] # value
        self.dict_value_pos = dict() # {key: [pos, time]}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.dict_value_pos:
            pos = self.dict_value_pos[key][0]
            value = self.cache[pos]
            self.dict_value_pos[key][1] = time.time()

        else:
            value =  -1
        
        print(value)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        now = time.time()
        if self.cache[-1] != None:
            pos = 0
            max_time = 0
            del_key = None

            if key in self.dict_value_pos:
                pos = self.dict_value_pos[key][0]
                self.dict_value_pos[key] = [pos, now]
                self.cache[pos] = value
                return 

            for _key in self.dict_value_pos:
                _pos, _time = self.dict_value_pos[_key]

                if max_time < now - _time:
                    max_time = now - _time
                    pos = _pos
                    del_key = _key

            del self.dict_value_pos[del_key]
            self.dict_value_pos[key] = [pos, now]
            self.cache[pos] = value
            return 

        else:
            for i in range(len(self.cache)):
                if self.cache[i] == None:
                    self.dict_value_pos[key] = [i, now]
                    self.cache[i] = value
                    return

    def get_cache(self):
        return self.cache

    def print_cache(self):
        print(self.cache)
        print(self.dict_value_pos)


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
our_cache.set(6, 7)
our_cache.print_cache()
# Test Case 2
our_cache.set(8, 7)
our_cache.print_cache()
# Test Case 3
our_cache.set('r', 'A')
our_cache.print_cache()