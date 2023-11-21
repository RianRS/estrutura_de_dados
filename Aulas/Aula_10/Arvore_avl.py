class treeNode:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1


class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
        else:
            root.r = self.insert(root.r, key)
        root.h = 1 + max(self.getHeight(root.l),
                         self.getHeight(root.r))
        b = self.getBal(root)