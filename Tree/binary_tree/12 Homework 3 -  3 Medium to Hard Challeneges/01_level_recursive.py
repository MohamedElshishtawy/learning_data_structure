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

    #######################################
    def _tree_height(self, current):
        if not current:
            return -1

        return 1 + max(self._tree_height(current.left), self._tree_height(current.right))

    def print_nodes_level(self, current, level):
        if not current:
            return

        if level == 0:
            print(current.val, end=' ')
        elif level:
            self.print_nodes_level(current.left, level - 1)
            self.print_nodes_level(current.right, level - 1)

    def level_order_traversal_recursive(self):  # O(n^2) time
        h = self._tree_height(self.root)
        # do traversal level by level. This is so slow
        # This solution is related to iterative deepening technique
        # where we can traverse but limit our self to a specific level

        for level in range(h + 1):
            print(f'\nLevel {level}: ', end='')
            self.print_nodes_level(self.root, level)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.add([2, 4, 8], ['L', 'L', 'L'])
    tree.add([2, 4, 9], ['L', 'L', 'R'])
    tree.add([2, 5, 10], ['L', 'R', 'L'])
    tree.add([2, 5, 11], ['L', 'R', 'R'])

    tree.add([3, 6, 12], ['R', 'L', 'L'])
    tree.add([3, 6, 13], ['R', 'L', 'R'])
    tree.add([3, 7, 14], ['R', 'R', 'L'])
    tree.add([3, 7, 15], ['R', 'R', 'R'])

    tree.level_order_traversal_recursive()




