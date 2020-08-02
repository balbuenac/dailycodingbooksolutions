# assumption: sorted list
def swap(prev, a, b):
    a.next = b.next
    b.next = a
    if prev:
        prev.next = b

def print_linked_list(root):
    while root:
        print(root.data)
        root = root.next

def swap_low_high(root):
    prev, curr, next = None, root, None
    i = 0
    while curr and curr.next:
        if curr.data < curr.next.data and (i % 2) != 0:
            print(i)
            temp = curr.next
            swap(prev, curr, curr.next)
            curr = temp
        prev = curr
        curr = curr.next
        i += 1

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

node4 = Node(5)
node3 =  Node(4, node4)
node2 = Node(3, node3)
node1 = Node(2, node2)
root = Node(1, node1)
print_linked_list(root)
swap_low_high(root)
print_linked_list(root)