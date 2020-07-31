def print_linked_list(root):
    while root:
        print(root.data)
        root = root.next

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

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node2 = Node(2)
node1 = Node(3, node2)
root = Node(5, node1)

print_linked_list(root)
print_linked_list(reverse_linked_list(root))
