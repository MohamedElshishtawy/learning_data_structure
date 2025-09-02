class Node:

    def __init__(self, value, left = None, right = None):
        self.value  = value
        self.left   = left
        self.right  = right
        self.height = 1
        self.count  = 1

    def _child_height(self, child):
        if not child:
            return -1
        return child.height 
    
    def child_count(self, child):
        if not child:
            return 0
        return child.count
    
    def _update_height(self):
        self.height = 1 + max(self._child_height(self.left), self._child_height(self.right))
        self.count  = 1 + self.child_count(self.left) + self.child_count(self.right) 

    def balance_factor(self):
        return self._child_height(self.left) - self._child_height(self.right)
    
    def is_leaf(self):
        return not self.left and not self.right



class AVL:

    root = None
    size = 0
    height = 0.

    def __init__(self, root_val):
        self.root = Node(root_val)
        self.size = 1
        

    def _right_rotaion(self, node):
        C = node.left
        right_side = C.right

        C.right = node
        node.left = right_side
        #update The height
        node._update_height()
        C._update_height()
        return C

    def _left_rotation(self, node):
        C = node.right           # ✓ Right child becomes new root
        left_side = C.left       # ✓ Save C's LEFT subtree  
        C.left = node           # ✓ Old root becomes LEFT child of C
        node.right = left_side   # ✓ Attach saved subtree to node's right
        node._update_height()
        C._update_height()
        return C

    def balace(self, node):
        if node.balance_factor() == 2:
            
            if node.left.balance_factor() == -1:
                node.left = self._left_rotation(node.left)
            
            node = self._right_rotaion(node)


        elif node.balance_factor() == -2:
            
            if node.right.balance_factor() == 1:
                node.right = self._right_rotaion(node.right)
            
            node = self._left_rotation(node)
        return node
        

    def insert(self, val):
        def _insert_to(parent, val):
            if parent.value < val:
                if parent.right :
                    parent.right = _insert_to(parent.right, val)
                else:
                    parent.right = Node(val)
            elif parent.value > val:
                if parent.left:
                    parent.left = _insert_to(parent.left, val)
                else:
                    parent.left = Node(val)

            parent._update_height()
            return self.balace(parent)
           
        self.root =  _insert_to(self.root, val)

    def delete(self, val):
        def process(current, val):
            if current.value < val:
                current.right = process(current.right, val)
                return current
            elif current.value > val:
                current.left = process(current.left, val)
                return current
            
            # We get the node
            if current.is_leaf():
                return None
            
            elif not current.left: # only right
                current = current.right

            elif not current.right: # only left
                current = current.left
                
            else: #left and right
                mn = self.minNode(current.right)
                current.value = mn.value
                current.right = process(current.right, mn.value)

            # return current
            current._update_height()
            return self.balace(current)


        self.root = process(self.root, val)
        

    def minNode(root, current):
        def process(current):
            if current.is_leaf():
                return current
            if current.left:
                return process(current.left)
            return current
        return process(current)


    def show(self):

        def _iterate(current):

            if not current:
                return
            
            if current.left:
                _iterate(current.left)
            
            print(f"{current.value}({current.height})", end=' ')

            if current.right:
                _iterate(current.right)

            
        _iterate(self.root)

    # Home work question 
    def lower_boundry(self, val):
        def process(current, val):
            if not current:
                return None
            
            if current.value >= val:   
                ans = process(current.left, val)
                if ans is not None:
                    return ans
                return current.value         
                # ---- my answer (wrong)
                # if not current.left or (current.left and current.left.value < val):
                #     return current.value
                # return process(current.left, val)    
            
            return process(current.right, val)

        return process(self.root, val) 
    
    def upper_boundry(self, val):
        def process(current, val):
            if not current:
                return None
        
            
            if current.value > val:   
                ans = process(current.left, val)
                if ans is not None:
                    return ans
                return current.value         
                # ---- my answer (wrong)
                # if not current.left or (current.left and current.left.value < val):
                #     return current.value
                # return process(current.left, val)    
            
            return process(current.right, val)

        return process(self.root, val) 
    
    def count(self, root = None):
        
        def process(root):
            if not root:
                return 0
            return 1 + process(root.left) + process(root.right)
        
        return process(root if root is not None else self.root)
    
    def count_greate(self, val):
        """Get the count of the elemnts thag greater than the val"""

        def process(val, current):
            if not current:
                return 0
            
            if current.value <= val:
                return process(val, current.right)
            else: 
                return 1 + current.child_count(current.right) + process(val, current.left) 
        
        return process(val, self.root)



avl = AVL(15)
values_to_insert =[ 10, 20, 5, 12, 11]
for val in values_to_insert:
    avl.insert(val)

avl.show()
print()
print(avl.count_greate(2))
