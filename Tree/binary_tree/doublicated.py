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

    def _print_all_similar(self, currnet, root):
        if not currnet or not root:
            return
        if currnet.value != root.value:
            return
        
        self._print_all_similar(currnet.left, root.left)
        print(currnet.value, end=' ')
        self._print_all_similar(currnet.right, root.right)
        print(currnet.value)


    def _is_doublicated_with(self, current, root):
        
        if not root:
            return
        if current.value == root.value and current != root:
            self._print_all_similar(current, root)
            print()

        self._is_doublicated_with(current, root.left)
        self._is_doublicated_with(current, root.right)
        
        return True

    def print_doublicated(self):
        def check_doublicated(current):
            if not current:
                return
            
            self._is_doublicated_with(current, self.root)
                

            check_doublicated(current.left)
            check_doublicated(current.right)
            return True
        
        check_doublicated(self.root)






tree = Tree(1)
tree.add([2, 3], ['L', 'L'])
tree.add([6, 5], ['R', 'L'])
tree.add([6, 2, 3], ['R', 'R', 'R'])


tree.print_doublicated()



