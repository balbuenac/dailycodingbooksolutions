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

def helper(root):
    q = [root]
    min_level = sys.maxsize
    while q:
        count = len(q)
        sum = 0
        while count > 0:
            curr = q.pop()
            if curr:
                sum = sum + curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            count = count - 1
        min_level = min(min_level, sum)
    return min_level

left_level_2 = Node(1)
right_level_2 = Node(2)
root_level_2 = Node(3, left_level_2, right_level_2)

left_level_1 = Node(4)
right_level_1 = Node(5)
root_level_1 = Node(2, left_level_1, right_level_1)

left = Node(1, root_level_1, root_level_2)
right = Node(1)
root = Node(3, left, right)
print(helper(root))
