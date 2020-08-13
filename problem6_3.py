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
    if not root:
        return
    print(root.val)
    if not root.val in ['+', '-', '*', '/']:
        # print(root.val)
        return int(root.val)

    if root and root.left and root.right:
        if root.val == '+':
            return helper(root.left) + helper(root.right)
        elif root.val == '-':
            return helper(root.left) - helper(root.right)
        elif root.val == '*':
            return helper(root.left) * helper(root.right)
        else:
            return helper(root.left) / helper(root.right)

left_level_2 = Node('1')
right_level_2 = Node('1')
root_level_2 = Node('*', left_level_2, right_level_2)

left_level_1 = Node('4')
right_level_1 = Node('5')
root_level_1 = Node('*', left_level_1, right_level_1)

left = Node('+', root_level_1, root_level_2)
right = Node('5')
root = Node('+', left, right)
print(helper(root))
