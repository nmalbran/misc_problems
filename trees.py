
class BinaryTreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "%d: (%s) (%s)" % (self.val, str(self.left), str(self.right))


def depth_first_search(tree_root, val_to_find):
    if tree_root is None:
        return False
    #print tree_root.val
    if tree_root.val == val_to_find:
        return True

    return depth_first_search(tree_root.left, val_to_find) or \
           depth_first_search(tree_root.right, val_to_find)


def breadth_first_search(tree_root, val_to_find):
    q = [tree_root]
    while len(q) > 0:
        n = q.pop(0)
        if n is None:
            return False

        #print n.val
        if n.val == val_to_find:
            return True
        else:
            q.append(n.left)
            q.append(n.right)

    return False


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def add(self, x):
        new_node = BinaryTreeNode(x)
        if self.root is None:
            self.root = new_node
            return

        new_pos = self.root
        while True:
            if x <= new_pos.val:
                if new_pos.left is None:
                    new_pos.left = new_node
                    return
                else:
                    new_pos = new_pos.left
            else:
                if new_pos.right is None:
                    new_pos.right = new_node
                    return
                else:
                    new_pos = new_pos.right

    def __str__(self):
        return str(self.root)


class RecursiveBinarySearchTreeNode(BinaryTreeNode):

    def add(self, x):
        if x <= self.val:
            if self.left is None:
                self.left = RecursiveBinarySearchTreeNode(x)
            else:
                self.left.add(x)
        else:
            if self.right is None:
                self.right = RecursiveBinarySearchTreeNode(x)
            else:
                self.right.add(x)

class RecursiveBinarySearchTree(object):
    def __init__(self):
        self.root = None

    def add(self, x):
        if self.root is None:
            self.root = RecursiveBinarySearchTreeNode(x)
        else:
            self.root.add(x)

    def __str__(self):
        return str(self.root)

def test_tree_search():
    i = BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5))
    d = BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7))
    r = BinaryTreeNode(1, i, d)
    print r
    nums_to_search = [1, 4, 7, 8]
    for i in nums_to_search:
        print "Depth First Search:"
        print depth_first_search(r, i)

        print "Breadth First Search:"
        print breadth_first_search(r, i)

def test_binary_search_tree():
    import random
    t = RecursiveBinarySearchTree()
    for i in range(20):
        t.add(random.randint(1,50))
    print t

if __name__ == '__main__':
    test_binary_search_tree()