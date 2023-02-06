# Task 1: Finding the Square Root of an Integer

### Explanation of code
We need to find the square root of an integer and choose the floor value if there is no integer soultion. There are two steps. First, we half the number if the half number squared is bigger than the original number until meeting the first half number squared is smaller than the number which can make the time complexity to O(log(n)). Second part is that we gradually reduce the number to find the first one which its squared number is less than the original number.

### Time and Space Complexity Analysis
The time and space complexity for this program is O(log(n)) because we find the half number each time.
