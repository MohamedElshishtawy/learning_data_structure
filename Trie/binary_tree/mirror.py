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

    def clone_right(main, right):
        main.right = right

    def clone_left(main, left):
        main.left = left


    def max(self):
        def iterate(current):
            if not current:
                return float('-inf')
            return max(current.value, iterate(current.left), iterate(current.right))
        return iterate(self.root)
    
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
         
    def print_post_order(self):
        def _print_post_order(current):
            if not current:
                return
            _print_post_order(current.left)
            _print_post_order(current.right)
            print(current.value, end=' ')
        _print_post_order(self.root)
        print('\n---------')

    def is_mirror(self):
        
        def are_mirrors(current1, current2):

            if not current1 and not current2:
                return True
            if (current1 and not current2) or (current2 and not current1):
                return False 
            if current1.value != current2.value:
                return False
            
            return are_mirrors(current1.left, current2.right) and are_mirrors(current1.right, current2.left)
            

        current1 = self.root.left
        current2 = self.root.right
        return are_mirrors(current1, current2)





tree = Tree(1)
tree.add([2, 5], ['L', 'L'])
tree.add([2, 6], ['L', 'R'])
tree.add([2, 6], ['R', 'L'])
tree.add([2, 5], ['R', 'R'])

print(tree.is_mirror())



