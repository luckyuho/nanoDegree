# Runtime Analysis

### Task 6: Union and Intersection of Two LinkedLists
- Worst-case time complexity is O(nlogn).
- The time complexity for this program is O(nlogn) because the length of our cache array is a fixed capacity.
  
```python
# # Example case 1
# arr1 = [3,2,4,35,6,65,6,4,3,21]
# arr2 = [6,32,4,9,6,1,11,21,1]
# print_union_and_intersection(arr1, arr2, "example1")
example1
[1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
[4, 6, 21]

# # Example case 2
# arr1 = [3,2,4,35,6,65,6,4,3,23]
# arr2 = [1,7,8,9,11,21,1]
# print_union_and_intersection(arr1, arr2, "example2")
example2
[1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
[]

# # Add your own test cases: include at least three test cases
# # and two of them must include edge cases, such as null, empty or very large values

# # Test Case 1
# arr1 = [1,-1,3,0,1]
# arr2 = [-1,4,6,8,23,0]
# print_union_and_intersection(arr1, arr2, "case1")
case1
[-1, 0, 1, 3, 4, 6, 8, 23]
[-1, 0]

# # Test Case 2
# arr1 = [3,2,4,35,6,65,6,4,3,23]
# arr2 = []
# print_union_and_intersection(arr1, arr2, "case2")
case2
[2, 3, 4, 6, 23, 35, 65]
[]

# # Test Case 3
# arr1 = [1,1,1,1,1,1]
# arr2 = [1,2,2,2,2,2]
# print_union_and_intersection(arr1, arr2, "case3")
case3
[1, 2]
[1]
```