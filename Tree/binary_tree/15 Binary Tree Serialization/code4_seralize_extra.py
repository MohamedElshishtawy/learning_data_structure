class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    # more efficient that the str, but harder to use in some problems
    def parenthesize(self):

        def _parenthesize(current):
            lst = [current.val]

            if current.left:
                lst.append(_parenthesize(current.left))
            else:
                lst.append(None)

            if current.right:
                lst.append(_parenthesize(current.right))
            else:
                lst.append(None)

            return lst

        return _parenthesize(self.root)

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


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 7], ['L', 'L', 'L'])
    tree.add([2, 4, 8], ['L', 'L', 'R'])
    tree.add([2, 5, 9], ['L', 'R', 'R'])
    tree.add([3, 6, 10], ['R', 'R', 'L'])

    print(tree.parenthesize())
    # [1, [2, [4, [7, None, None], [8, None, None]], [5, None, [9, None, None]]], [3, None, [6, [10, None, None], None]]]


