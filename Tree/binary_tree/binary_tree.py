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

    def max_depth(self):
        def get_depth(current):
            if not current:
                return 0
            return 1+ max(get_depth(current.left), get_depth(current.right))
        return get_depth(self.root)
    

    def sum_of_leaves(self):
        def iterate(current, is_left=False):
            if not current:
                return 0
            if not current.left and not current.right:
                return current.value if is_left else 0
            return iterate(current.left, True) + iterate(current.right)
        return iterate(self.root)


    def isCouison(self, x, y):
        # مش عارف احلها
        pass

    def is_perfect(self):
        def iterate(current, height):
            if not current:
                return True
            
            # is leaf
            if not current.left and not current.right:
                return height == 1
                
            
            
            return iterate(current.left, height-1) and \
                iterate(current.right, height-1)

        height = self.max_depth()
        return iterate(self.root, height)

    def _number_of_nodes(self):
        def iterate(current):
            if not current:
                return 0
            return 1 + iterate(current.left) + iterate(current.right)
        return iterate(self.root)
    
    def is_perfect_2(self):
        def _height():
            def itearte(current):
                if not current:
                    return 0
                return 1+ itearte(current.left)
            return itearte(self.root) -1
     
        h = _height()
        n = self._number_of_nodes()
        return n == (2**(h+1)-1)
    
    def in_order_iterative(self):
        res = []
        storage = []

        storage.append([self.root, False])

        while storage:
            current, is_vertix = storage[-1]
            storage.pop()

            if is_vertix:
                res.append(current.value)
            else:
                storage.append([current.right, False]) if current.right else None
                storage.append([current, True])
                storage.append([current.left, False]) if current.left else None 
        return res
    
    def left_tree_boundary(self):
        res = []
        def iterate(current):
            if not current:
                return
            res.append(current.value)
            return iterate(current.left) if current.left else iterate(current.right)
        iterate(self.root)
        return res
    
    def get_diameter(self):
        self.diameter = 0
        
        def height(current):
            if not current:
                return 0

            lheight = height(current.left)
            rheight = height(current.right)
            self.diameter = max(self.diameter, lheight+rheight)

            return 1 + max(height(current.left), height(current.right))
        
        height(self.root)
        return self.diameter

    def diameterOfBinaryTree(self):
        self.diameter = 0
        self.calc_diameter(self.root)
        return self.diameter

    def calc_diameter(self, current):
            if not current:
                return 0
            
            l_height = self.calc_diameter(current.left)
            r_height = self.calc_diameter(current.right)

            self.diameter = max(self.diameter, l_height+r_height)

            return 1+ max(l_height, r_height)
        




tree = Tree(1)
tree.add([2], ['L'])
tree.add([3, 4], ['R', 'L'])

print(tree.diameterOfBinaryTree())


# # left tree boundary test

# def test1():
#     tree = Tree(1)
#     tree.add([2, 4, 7], ['L', 'L', 'L'])
#     tree.add([2, 4, 8], ['L', 'L', 'R'])
#     tree.add([2, 5, 9], ['L', 'R', 'R'])
#     tree.add([3, 6, 10], ['R', 'R', 'L'])

#     assert tree.left_tree_boundary() == [1, 2, 4, 7]
# test1()

