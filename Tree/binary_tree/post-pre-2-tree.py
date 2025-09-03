class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    root = None
    def __init__(self):
        pass

    def _is_leaf(self, node):
        return node and not node.left and not node.right 

    def pre_in_2_binary(self, preorder, inorder):
        if not inorder:
            return None
        
        root = TreeNode(preorder.pop(0))
        pos  = inorder.index(root.val)

        if not self.root:
            self.root = root

        root.left = self.pre_in_2_binary(preorder, inorder[:pos])
        root.right = self.pre_in_2_binary(preorder, inorder[pos+1:])

        return root

    
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

            print(current.val, end='')
            if current.right:
                if self._is_leaf(current.right):
                    print('(', end='')
                iterate(current.right)
                if self._is_leaf(current.right):
                    print(')', end='')

        return iterate(self.root)
    

tr = Tree()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tr.pre_in_2_binary(preorder, inorder)
tr.print_in_order()
