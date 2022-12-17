class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    l1 = llist_1.head
    l2 = llist_2.head
    union_dict = dict()

    record_list_to_dict(l1, union_dict)
    record_list_to_dict(l2, union_dict)

    output_list = []
    for k in union_dict:
        output_list.append(k)

    output_list = sorted(output_list)

    return output_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    l1 = llist_1.head
    l2 = llist_2.head

    dict1 = dict()
    record_list_to_dict(l1, dict1)

    dict2 = dict()
    record_list_to_dict(l2, dict2)

    output_list = []
    for k in dict1:
        if k in dict2:
            output_list.append(k)

    output_list = sorted(output_list)

    return output_list

def record_list_to_dict(record_list, record_dict):
    list_head = record_list
    
    while list_head:
        value = list_head.value
        record_dict[value] = True
        list_head = list_head.next

    return

def print_union_and_intersection(arr1, arr2, case):
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    for i in arr1:
        linked_list1.append(i)

    for i in arr2:
        linked_list2.append(i)

    print(case)
    print (union(linked_list1,linked_list2))
    print (intersection(linked_list1,linked_list2))


# Example case 1
arr1 = [3,2,4,35,6,65,6,4,3,21]
arr2 = [6,32,4,9,6,1,11,21,1]
print_union_and_intersection(arr1, arr2, "example1")

# Example case 2
arr1 = [3,2,4,35,6,65,6,4,3,23]
arr2 = [1,7,8,9,11,21,1]
print_union_and_intersection(arr1, arr2, "example2")

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
arr1 = [1,-1,3,0,1]
arr2 = [-1,4,6,8,23,0]
print_union_and_intersection(arr1, arr2, "case1")

# Test Case 2
arr1 = [3,2,4,35,6,65,6,4,3,23]
arr2 = []
print_union_and_intersection(arr1, arr2, "case2")

# Test Case 3
arr1 = [1,1,1,1,1,1]
arr2 = [1,2,2,2,2,2]
print_union_and_intersection(arr1, arr2, "case3")
