# Task 6: Union and Intersection of Two LinkedLists

### Explanation of code
There are two cases in this project: union and intersection of two arrays. In union method, we use same dict to record data, so if data shows in dict, it means there must appear at least one array. In intersection, we use two dicts, it shows the elements exist in both of the dicts.

### Time and Space Complexity Analysis
The time and space complexity for this program is O(n*log(n)).

### Result
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
### Question
1. In fact, I have no idea why we use link list to deal this problem, is there any better way to deal with this problem?
2. I think time and space complexity are the same at most time. When will it be difference?
