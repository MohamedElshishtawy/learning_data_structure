class Node:
    left = None
    right = None
    value = 0

    def __init__(self, left=None, right=None, value=None, parent=None):
        self.left = left
        self.right = right
        self.value = value
        self.parent = parent


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
                    prev.left = Node(None, None, value, prev)
                elif prev.left.value != value:
                    print(value , prev.left.value)
                    raise TypeError(f"Left not correct for {value}")
                prev = prev.left
            else:
                if  not prev.right:
                    prev.right = Node(None, None, value, prev)
                elif prev.right.value != value:
                    raise TypeError(f"Right not correct for {value}")
                prev = prev.right
            
    
    def smallest(self, target=None):
        def iterate(current):
            if not current:
                return
            if not current.left:
                return current.value
            return iterate(current.left)
        return iterate(self.root) if not target else iterate(target)
    
    def _find_ansessors_chain(self, target):
        
        def iterate(current):
            # target node not found
            if not current:
                return False
            
            # add to the anssesrs
            self.ansessors.append(current)

            # target has been founded
            if current.value == target:
                return True
            
            if current.value > target:
                return iterate(current.left)
            return iterate(current.right)

        current = self.root
        self.ansessors = []
        if iterate(current):
            return self.ansessors
        return []

    def successor(self, target):
        # if you have right tree 
            # get the min
        # if you dont have right 
            # if you are a right child
                # get the first parent with diffrent position
            # if you are a left child
                # get the first parent
        ansessors = self._find_ansessors_chain(target)
        target = ansessors.pop()

        if target.right:
            min_val = self.smallest(target.right)
            return min_val
        
        parent = target.parent

        if parent.right and parent.right.value == target.value:
            child = target
            while parent.right and parent.right.value == child.value:
                child  = parent
                parent = None if not ansessors else parent.parent

            if not parent:
                return None 
            return parent.value
        elif parent.left and parent.left.value == target.value:
            return parent.value

        return None


    
            


tr = Tree(10)
tr.add([2, 1], ['L', 'L'])
tr.add([2, 5], ['L', 'R'])
tr.add([13], ['R'])
print(tr.successor(5))
### Checkpoint
# we debuf the first condition only r


        
