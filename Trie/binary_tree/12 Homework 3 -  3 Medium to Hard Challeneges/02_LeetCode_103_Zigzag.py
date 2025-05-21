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
    def zigzagLevelOrder(self, root):
        import collections
        nodes_queue = collections.deque()
        nodes_queue.append(root)
        level, forward_level = 0, True
        ans = []

        while nodes_queue:
            row = []
            sz = len(nodes_queue)

            for step in range(sz):
                if forward_level:
                    # Usual queue style: pop queue front, push queue rear: left, then right
                    cur = nodes_queue.popleft()
                    row.append(cur.val)

                    if cur.left:
                        nodes_queue.append(cur.left)
                    if cur.right:
                        nodes_queue.append(cur.right)
                else:
                    # like Stack: pop stack end, push stack front: right, then left
                    cur = nodes_queue.pop()
                    row.append(cur.val)
                    # observe from the end, the right comes before left. Use appendleft
                    if cur.right:
                        nodes_queue.appendleft(cur.right)
                    if cur.left:
                        nodes_queue.appendleft(cur.left)

            level, forward_level = level+1, not forward_level
            ans.append(row)

        return ans




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

    print(Solution().zigzagLevelOrder(tree.root))





