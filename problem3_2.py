res = 0
def reverse_linked_list(root):
    if not root:
        return None

    if not root.next:
        return root

    curr, prev, next = root, None, root.next
    while curr:
        curr.next = prev
        prev = curr
        curr = next
        if curr:
            next = curr.next
    return prev

def print_linked_list(root):
    while root:
        print(root.data)
        root = root.next

def add_nodes(root, root2, mod, ind, result):
    if not root and not root2:
        if mod == 0:
            # print(result)
            global res
            res = result
        sum = mod

    if root and root2:
        sum = root.data + root2.data + mod
    elif root:
        sum = root.data + mod
    elif root2:
        sum = root2.data + mod

    if sum > 0:
        new_mod = sum // 10
        result = result +  (sum % 10) * 10 ** ind
        add_nodes(root.next if root else None, root2.next if root2 else None, new_mod, ind+1, result)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node2 = Node(9)
node1 = Node(9, node2)
root = Node(9, node1)

node4 = Node(2)
node3 = Node(3, node4)
root2 = Node(5, node3)

#print_linked_list(root)
#print_linked_list(root2)
result = 0
add_nodes(reverse_linked_list(root), reverse_linked_list(root2), 0, 0, result)
print(res)
