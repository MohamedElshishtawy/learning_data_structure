# https://leetcode.com/problems/symmetric-tree/

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add(self, values_lst, direction_lst):
        assert len(values_lst) == len(direction_lst)

        current = self.root
        # iterate on the path, all necessary nodes
        for i, val in enumerate(values_lst):
            if direction_lst[i] == 'L':
                if not current.left:
                    current.left = Node(values_lst[i])
                else:
                    assert current.left.val == values_lst[i]
                current = current.left
            else:
                if not current.right:
                    current.right = Node(values_lst[i])
                else:
                    assert current.right.val == values_lst[i]
                current = current.right


class Solution(object):
    def isSymmetric(self, root):
        def is_mirror(first, second):
            if not first and not second:
                return True
            if first and not second or not first and second:
                return False
            if first.val != second.val:
                return False

            return is_mirror(first.left, second.right) and is_mirror(first.right, second.left)

        return is_mirror(root.left, root.right)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([12, 4, 7], ['L', 'L', 'L'])
    tree.add([12, 4, 8], ['L', 'L', 'R'])
    tree.add([12, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])
