# Task 4: Active Directory

### Explanation of code
This problem ask to know the member in group, besides, the group can contain other groups. If we want to know whether this person is in this group, we need to find the member in the group and those members in the other groups which the group contains. Therefore, we use recursion to find the group and its sub groups.

### Time and Space Complexity Analysis
The time and space complexity for this program is O(n) because it will traverse all other groups belong to the group.

### Result  
```python
# A = Group("A")
# B = Group("B")

# A.add_user("Alan")
# A.add_user("Amy")

# B.add_user("Bob")
# B.add_user("Betty")

# Class = Group("class")

# # Test Case 1 # check group member itself, expected True
# print_is_user_in_group("Amy", A)
user: Amy is in group A
True
# # Test Case 2 # A -> B -> C, expected True
# C = Group("C")
# C.add_user("Calvin")
# C.add_user("Cathy")
# B.add_group(A)
# C.add_group(B)
# print_is_user_in_group("Amy", C)
user: Amy is in group A
True
# # Test Case 3 # A -> B -> 
# #                         C -> E
# #                    D -> 
# # check member in D, expected True
# # Noted: Something should be careful where I noted above
# D = Group("D")
# D.add_user("David")
# D.add_user("Denise")

# C.add_group(D)

# E = Group("E")
# E.add_user("Eden")
# E.add_user("Eve")
# E.add_group(C)

# print_is_user_in_group("David", E)
user: David is in group D
True
```