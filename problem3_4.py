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

def swap(prev, a, b):
    a.next = b.next
    b.next = a
    if prev:
        prev.next = b

def print_linked_list(root):
    while root:
        print(root.data)
        root = root.next

def intersection(rootA, rootB):
    rootA_ = reverse_linked_list(rootA)
    rootB_ = reverse_linked_list(rootB)
    res = None
    while rootA_ and rootB_ and rootA_.data == rootB_.data:
        res = rootA_.data
        rootA_ = rootA_.next
        rootB_ = rootB_.next
    return res
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

node4 = Node(5)
node3 =  Node(4, node4)
node2 = Node(13, node3)
node1 = Node(2, node2)
root = Node(1, node1)
#print_linked_list(root)
node4 = Node(5)
node3 =  Node(4, node4)
node2 = Node(10, node3)
node1 = Node(7, node2)
root2 = Node(99, node1)
#swap_low_high(root)
#print_linked_list(root2)
print(intersection(root, root2))