import random

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    QuickSort(input_list)
    right_digit = len(input_list) // 2
    left_digit = right_digit if len(input_list) % 2 == 0 else right_digit + 1
    left_num, right_num = 0, 0
    for i, val in enumerate(input_list):
        if i % 2 == 0:
            left_num += pow(10, left_digit-1)*val
            left_digit -= 1
        else:
            right_num += pow(10, right_digit-1)*val
            right_digit -= 1
    return [left_num, right_num]


def QuickSort(arr):
    quick_sort(arr, 0, len(arr)-1)

def quick_sort(arr, left, right):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort(arr, left, pivot-1)
    quick_sort(arr, pivot+1, right)


def partition(arr, left, right):
    pivot = right
    pivot_val = arr[pivot]
    index = left

    for i in range(left, right):
        if arr[i] > pivot_val:       
            arr[index], arr[i] = arr[i], arr[index]
            index += 1

    arr[right], arr[index] = arr[index], arr[right]

    return index
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
