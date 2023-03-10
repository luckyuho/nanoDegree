## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix == "":
        return []

    output = list()
    return _find_files(suffix, path, output)
    

def _find_files(suffix, path, output):
    if os.path.isdir(path):
        dirFile = os.listdir(path)
    
        for i in dirFile:
            path_i = os.path.join(path, i)

            if not os.path.isfile(path_i):
                _find_files(suffix, path_i, output)

            if path_i.endswith(suffix):
                output.append(path_i)

        return output

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
root_path = "./DataStructAndAlgorithm/P1/Task2"
# Test Case 1
output = find_files(".c", root_path)
print(output)
# Test Case 2
output = find_files(".h", root_path)
print(output)
# Test Case 3
output = find_files("", root_path)
print(output)