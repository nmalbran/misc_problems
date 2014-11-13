
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


if __name__ == '__main__':
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
