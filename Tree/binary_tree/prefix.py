class Node:
    left = None
    right = None
    value = 0

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self, prefix):
        nodes_stk = []
        
        for char in prefix:
            node = Node(value=char)

            if not char.isdigit():
                node.right = nodes_stk.pop()
                node.left = nodes_stk.pop()
            nodes_stk.append(node)
        assert len(nodes_stk) == 1
        self.root = nodes_stk.pop()
    def showBinary(self):
        def iterate(current):
            if not current:
                return
            
            if current.left:
                iterate(current.left)
            
            if current.right:
                iterate(current.right)

            print(current.value, end='')

        return iterate(self.root)
    def _is_leaf(self, node):
        return node and not node.left and not node.right 
    
    def print_in_order(self):
        def iterate(current):
            if not current:
                return
            if current.left:
                if not self._is_leaf(current.left):
                    print('(', end='')

                iterate(current.left)
                
                if not self._is_leaf(current.left):
                    print(')', end='')

            print(current.value, end='')
            if current.right:
                if self._is_leaf(current.right):
                    print('(', end='')
                iterate(current.right)
                if self._is_leaf(current.right):
                    print(')', end='')

        return iterate(self.root)


bt = BinaryTree('23+4*')
bt.print_in_order()

