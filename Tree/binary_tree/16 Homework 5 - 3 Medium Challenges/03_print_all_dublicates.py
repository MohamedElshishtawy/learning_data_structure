

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

    def print_duplicate_subtrees(self):
        def _parenthesize(current):
            if not current:
                return ''

            if current.left:
                lrepr = _parenthesize(current.left)
            else:
                lrepr = '()'

            if current.right:
                rrepr = _parenthesize(current.right)
            else:
                rrepr = '()'

            repr = '(' + str(current.val) + lrepr + rrepr + ')'

            if current.left or current.right:
                if repr in dct:
                    dct[repr] += 1
                else:
                    dct[repr] = 1

            return repr

        # just traverse, get repr and add to dictionary
        dct = {}
        _parenthesize(self.root)
        lst = [item for item in dct.keys() if dct[item] > 1]
        print(lst)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 3], ['L', 'L'])
    tree.add([4, 5, 6, 8, 9], ['R', 'R', 'R', 'R', 'R'])
    tree.add([4, 2, 3], ['R', 'L', 'L'])
    tree.add([4, 5, 6, 7], ['R', 'R', 'L', 'L'])
    tree.add([4, 5, 6, 8, 9], ['R', 'R', 'L', 'R', 'R'])
    tree.add([4, 5, 6, 7], ['R', 'R', 'R', 'L'])

    tree.print_duplicate_subtrees()
    # ['(2(3()())())', '(8()(9()()))', '(6(7()())(8()(9()())))']
