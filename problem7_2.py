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

def helper(arr, l , r):
    if l < 0 or l >= len(arr):
        return
    if r < 0 or r >= len(arr):
        return
    if l > r:
        return
    pos = (l + r) // 2
    root = Node(arr[pos])
    root.left = helper(arr, l, pos-1)
    root.right = helper(arr, pos+1, r)
    return root

in_order = [-1, 5, 6, 7, 9, 10, 25]
root = helper(in_order, 0, len(in_order)-1)
print_tree(root)