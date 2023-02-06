def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    small_number = sqrt_target_big(number, number)
    target_value = sqrt_target_small(small_number, number)
    return target_value
    

def sqrt_target_big(num, target):
    if num * num == target:
        return num
    elif num * num < target:
        return num * 2
    
    return sqrt_target_big(num // 2, target)

def sqrt_target_small(num, target):
    if num * num == target:
        return num
    if num * num > target:
        return num - 1

    return sqrt_target_small(num + (num // 2), target)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")