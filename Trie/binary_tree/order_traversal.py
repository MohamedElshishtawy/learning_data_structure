class Node:
    left = None
    right = None
    value = 0

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value
class Tree:
    root = None
    def __init__(self, root_value):
        self.root = Node(None, None, root_value)
    def add(self, values_arr, dir_arr):
        assert len(values_arr) == len(dir_arr)
        prev = self.root
        for i, value in enumerate(values_arr):
            if dir_arr[i] == 'L':
                if not prev.left:
                    prev.left = Node(None, None, value)
                elif prev.left.value != value:
                    print(value , prev.left.value)
                    raise TypeError(f"Left not correct for {value}")
                prev = prev.left
            else:
                if  not prev.right:
                    prev.right = Node(None, None, value)
                elif prev.right.value != value:
                    raise TypeError(f"Right not correct for {value}")
                prev = prev.right

    def order_traversal(self):
        import collections
        nodeQueues = collections.deque()
        nodeQueues.append(self.root)
        level = 0

        # time complexity O(n)
        while nodeQueues:
            sz = len(nodeQueues)
            print(f"Level {level}: ", end='')
            for i in range(sz):
                current = nodeQueues[0]
                if current.left:
                    nodeQueues.append(current.left)
                if current.right:
                    nodeQueues.append(current.right)
                print(nodeQueues.popleft().value, end= '')
            level += 1
            print()

    def zigzag(self):
        import collections
        queue = collections.deque()
        result = []
        from_left = True
        level = 0
        queue.append(self.root)
        while queue:
            sz = len(queue)
            result.append([])
            for i in range(sz):
                current = queue[0]
                queue.popleft()
                if (from_left):
                    queue.append(current.right) if current.right else None
                    queue.append(current.left) if current.left else None
                else:
                    queue.append(current.left) if current.left else None
                    queue.append(current.right) if current.right else None
                    
                result[level].append(current.value)
                
            level += 1
            from_left = not from_left
        return result




tree = Tree(1)
tree.add([2], ['L'])
tree.add([3, 4], ['R', 'L'])
print(tree.zigzag())