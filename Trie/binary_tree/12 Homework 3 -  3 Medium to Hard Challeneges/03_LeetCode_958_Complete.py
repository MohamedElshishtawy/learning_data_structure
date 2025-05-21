# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
    def isCompleteTree(self, root):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(root)

        # Once there is a single missing node (left before right)
        # Nothing else should be there: on this level or next level
        no_more_allowed = False

        while nodes_queue:
            for step in range(len(nodes_queue)):
                cur = nodes_queue.popleft()

                if cur.left:
                    if no_more_allowed:
                        return False
                    nodes_queue.append(cur.left)
                else:
                    no_more_allowed = True

                if cur.right:
                    if no_more_allowed:
                        return False
                    nodes_queue.append(cur.right)
                else:
                    no_more_allowed = True

        return True




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




