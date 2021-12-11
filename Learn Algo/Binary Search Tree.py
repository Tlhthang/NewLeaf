class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


ro = Node(20)
ro = insert(ro, 31)
ro = insert(ro, 40)
ro = insert(ro, 8)
ro = insert(ro, 4)
ro = insert(ro, 19)
ro = insert(ro, 21)

inorder(ro)