# Runtime Analysis

### Task 1: Least Recently Used Cache
- We give each cache a timestamp, if cache is fulfill, the earliest timestamp of cache will be replace and if there is ever using a cache, we will renew its timestamp.
- Worst-case time complexity is O(1).
- The time complexity for this program is O(1) because the length of our cache array is a fixed capacity.
  
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
[1, 2, 7, 4, 5]
{1: [0, 1670763804.6052868], 2: [1, 1670763804.605301], 4: [3, 1670763804.605286], 5: [4, 1670763804.6053052], 6: [2, 1670763804.60531]}
# # Test Case 2
# our_cache.set(8, 7)
# our_cache.print_cache()
[1, 2, 7, 7, 5]
{1: [0, 1670763804.6052868], 2: [1, 1670763804.605301], 5: [4, 1670763804.6053052], 6: [2, 1670763804.60531], 8: [3, 1670763804.605324]}
# # Test Case 3
# our_cache.set('r', 'A')
# our_cache.print_cache()
['A', 2, 7, 7, 5]
{2: [1, 1670763804.605301], 5: [4, 1670763804.6053052], 6: [2, 1670763804.60531], 8: [3, 1670763804.605324], 'r': [0, 1670763804.605333]}
```