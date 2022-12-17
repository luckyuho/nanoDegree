# Runtime Analysis

### Task 2: Finding Files
- We use recursive way to access all files under the folders.
- Worst-case time complexity is O(n).
- The time complexity for this program is O(n) because the length of our cache array is a fixed capacity.
  
```python
# # Test Case 1
# output = find_files(".c", "./Task2")
# print(output)
['./Task2/testdir/subdir3/subsubdir1/b.c', './Task2/testdir/t1.c', './Task2/testdir/subdir5/a.c', './Task2/testdir/subdir1/a.c']
# # Test Case 2
# output = find_files(".h", "./Task2")
# print(output)
['./Task2/testdir/subdir3/subsubdir1/b.h', './Task2/testdir/subdir5/a.h', './Task2/testdir/t1.h', './Task2/testdir/subdir1/a.h']
# # Test Case 3
# output = find_files("", "./Task2")
# print(output)
[]
```