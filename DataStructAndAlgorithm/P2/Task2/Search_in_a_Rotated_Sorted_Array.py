def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)
    left = 0
    right = length - 1

    while (left <= right):
        mid = left + (right - left) // 2
        
        l_val = input_list[left]
        m_val = input_list[mid]
        r_val = input_list[right]

        # get answer
        if number == l_val:
            return left
        elif number == m_val:
            return mid
        elif number == r_val:
            return right

        if l_val <= m_val:
            if l_val < number < m_val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if m_val < number < r_val:
                left = mid + 1
            else:
                right = mid - 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test Edge Cases
test_function([[], 0])
test_function([[0,0,0], 0])