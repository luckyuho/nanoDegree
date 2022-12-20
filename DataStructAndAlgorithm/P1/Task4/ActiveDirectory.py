class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    # user of self group 
    if user in group.get_users():
        print(f'user: {user} is in group {group.get_name()}')
        return True

    status = False

    for g in group.get_groups():

        if user in g.get_users():
            print(f'user: {user} is in group {g.get_name()}')
            return True

        if g != []:
            status = is_user_in_group(user, g)
            if status: 
                return True
            # return False or status   # This would cause problem in case 3, which may cause an early closure.

    return False or status

def print_is_user_in_group(user, group):
    status = is_user_in_group(user, group)
    print(status)

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
A = Group("A")
B = Group("B")

A.add_user("Alan")
A.add_user("Amy")

B.add_user("Bob")
B.add_user("Betty")

Class = Group("class")

# Test Case 1 # check group member itself, expected True
print_is_user_in_group("Amy", A)

# Test Case 2 # A -> B -> C, expected True
C = Group("C")
C.add_user("Calvin")
C.add_user("Cathy")
B.add_group(A)
C.add_group(B)
print_is_user_in_group("Amy", C)

# Test Case 3 # A -> B -> 
#                         C -> E
#                    D -> 
# check member in D, expected True
# Noted: Something should be careful where I noted above
D = Group("D")
D.add_user("David")
D.add_user("Denise")

C.add_group(D)

E = Group("E")
E.add_user("Eden")
E.add_user("Eve")
E.add_group(C)

print_is_user_in_group("David", E)