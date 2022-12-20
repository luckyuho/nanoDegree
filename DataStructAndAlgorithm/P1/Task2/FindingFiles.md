# Task 2: Finding Files

### Explanation of code
We traverse all files under the folder. We use recursion way to access subfolder until no other subfolder.

### Time and Space Complexity Analysis
The time and space complexity for this program is O(n) because it will traverse all files.

### Result
```python
# root_path = "./DataStructAndAlgorithm/P1/Task2"
# # Test Case 1
# output = find_files(".c", root_path)
# print(output)
['./Task2/testdir/subdir3/subsubdir1/b.c', './Task2/testdir/t1.c', './Task2/testdir/subdir5/a.c', './Task2/testdir/subdir1/a.c']
# # Test Case 2
# output = find_files(".h", root_path)
# print(output)
['./Task2/testdir/subdir3/subsubdir1/b.h', './Task2/testdir/subdir5/a.h', './Task2/testdir/t1.h', './Task2/testdir/subdir1/a.h']
# # Test Case 3
# output = find_files("", root_path)
# print(output)
[]
```