

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
    def flipEquiv(self, root1, root2):
        def _parenthesize(current):
            if not current:
                return ''

            repr = '(' + str(current.val)

            if current.left:
                lrepr = _parenthesize(current.left)
            else:
                lrepr = '()'

            if current.right:
                rrepr = _parenthesize(current.right)
            else:
                rrepr = '()'

            if lrepr < rrepr:
                repr += lrepr + rrepr + ')'
            else:
                repr += rrepr + lrepr + ')'

            return repr

        first = _parenthesize(root1)
        second = _parenthesize(root2)

        return first == second
        #  We can also develop a recursive code that is based on
        #  is_flip_equiv(left, other.left) and is_flip_equiv(right, other.right) or
        #  is_flip_equiv(left, other.right) and is_flip_equiv(right, other.left)
        #  O(min(n, m)) where n & m are the 2 trees number of nodes
        #  This is NOT O(n^2) code. Think like preorder traversal


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([12, 4, 7], ['L', 'L', 'L'])
    tree.add([12, 4, 8], ['L', 'L', 'R'])
    tree.add([12, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])
