# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root = Node(preorder.pop(0))
        pos = inorder.index(root.val)

        root.left = self.buildTree(preorder, inorder[:pos])
        root.right = self.buildTree(preorder, inorder[pos + 1:])

        return root

    """
    We can make this code much more efficient as following:
    1- Convert the preorder to a dequeue, to allow efficient pop_left O(1)
    2- Instead of slicing, just pass the current start/end in the inorder list
    
    Another sol - Optional to check
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/212505/Python-solution 
    """

