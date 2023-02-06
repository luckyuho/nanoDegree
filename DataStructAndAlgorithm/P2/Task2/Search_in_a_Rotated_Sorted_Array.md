# Task 2: Search in a Rotated Sorted Array

### Explanation of code
Searching the index of the specific number in a rotated sorted array. Rotated sorted array means a sorted array which is rotated at some random pivot point, like [4,5,6,7,0,1,2]. That means there is only one part is not continuous. First, we use three pointers to divide array into two parts, continuous part and not continuous part. If the number is in the continuous part, if it's in the left part, we move the right pointer to get closer. Likewise, if it's in the right part, then we move left pointer.

### Time and Space Complexity Analysis
The time complexity is O(log(n)) because we find half amount each time. The space complexity is O(n).
