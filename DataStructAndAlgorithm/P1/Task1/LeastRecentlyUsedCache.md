# Task 1: Least Recently Used Cache

### Explanation of code
We give each cache a timestamp, if cache is fulfill, the earliest timestamp of cache will be replace and if there is ever using a cache, we will renew its timestamp.

This problem implements the Least Recently Used (LRU) Cache with an array plus a map. Array is used to record cache value, map is used to record the position and timestamp of the cache value accordingly. Adding the map triples the space complexity but makes the time efficiency for getting operations constant.

### Time and Space Complexity Analysis
The time and space complexity for this program is O(1) because the length of our cache array is a fixed capacity.

### Result
```python
# our_cache.get(1)
1
# our_cache.get(2)
2
# our_cache.get(9) 
-1
# our_cache.get(3)
-1

# # Test Case 1
# our_cache.set(6, 7)
# our_cache.print_cache()
OrderedDict([(6, 7), (5, 5), (2, 2), (1, 1), (4, 4)])
# # Test Case 2
# our_cache.set(8, 7)
# our_cache.print_cache()
OrderedDict([(8, 7), (6, 7), (5, 5), (2, 2), (1, 1)])
# # Test Case 3
# our_cache.set('r', 'A')
# our_cache.print_cache()
OrderedDict([('r', 'A'), (8, 7), (6, 7), (5, 5), (2, 2)])
```
### Question
1. In fact, in your reviews, you mention you use doubly link list, I have no idea what is its benefit, is there any better way to deal with this problem?