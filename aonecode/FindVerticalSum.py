import sys

class newNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

def verticalSum(root):
    print("VerticalSum")
    basekey = sys.maxsize // 2
    q = []
    h = {}
    # h[basekey] = root.val
    curr_key = basekey
    q.append((curr_key, root))
    while q:
        curr = q.pop(0)
        if curr:
            curr_key = curr[0]
            node = curr[1]
            if not curr_key in h:
                h[curr_key] = 0
            h[curr_key] += node.data
            if node.left:
                q.append((curr_key-1, node.left))
            if node.right:
                q.append((curr_key+1, node.right))

    result = []
    for k in sorted(h):
        result.append(h[k])

    return result

if __name__ == "__main__":

    '''      Create the following Binary Tree
              1
            /    \
          2        3
         / \      / \
        4   5    6   7
    '''
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)

    print("Following are the values of vertical "
          "sums with the positions of the "
          "columns with respect to root")

    print(verticalSum(root))
