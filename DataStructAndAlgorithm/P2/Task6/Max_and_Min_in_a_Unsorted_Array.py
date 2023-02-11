def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1:
        return None

    min_val = ints[0]
    max_val = ints[0]
    for val in ints:
        if min_val > val:
            min_val = val
        elif max_val < val:
            max_val = val

    return (min_val, max_val)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Test Edge Cases
l = []
print ("Pass" if (None == get_min_max(l)) else "Fail")
l = [1]
print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")
