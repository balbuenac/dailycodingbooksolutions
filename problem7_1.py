import sys


class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def helper(root, value, ceil, floor):
    if root is None:
        return ceil, floor

    if root.val == value:
        return root.val, root.val
    elif root.val < value:
        return helper(root.right, value, root.val, ceil)
    else:
        return helper(root.left, value, root.val, ceil)

    return ceil, floor


root_level_2 = Node(6, None, None)
root_level_1 = Node(-2, None, None)
root_level_right = Node(25, None, None)
left = Node(5, root_level_1, root_level_2)
right = Node(10, None, root_level_right)
root = Node(7, left, right)
#print_tree(root)
print(helper(root, 8, -1, -1))
