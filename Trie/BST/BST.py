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

    def pree_order_arr(self, current, result = []):
        if not current:
            return
        result.append(current.value)
        self.pree_order_arr(current.left)
        self.pree_order_arr(current.right)
        return result

    def find(self, val):
        current = self.root
        while current:
            if current.value == val:
                return self.pree_order_arr(current)
            elif current.value < val:
                current = current.right
            else:
                current = current.left

        return []
    def valid_BST(self):
        def is_valid(current, mn=float('-inf'), mx=float('inf')):
            if not current:
                return True

            current_val = current.value
            
            if not (mn < current_val < mx):
                return False


            return is_valid(current.left, mn, current_val) and is_valid(current.right, current_val, mx)
        return is_valid(self.root)
    
    def sorted2BST(self, nums):
        def process(nums):
            if len(nums) == 0:
                return None
            mid = len(nums) // 2
            return Node(nums[mid], process(nums[:mid]), process(nums[mid+1:]))
        return process(nums)
    
    def smallest(self, target=None):
        def iterate(current):
            if not current:
                return
            if not current.left:
                return current.value
            return iterate(current.left)
        return iterate(self.root) if not target else iterate(target)
    
    def kth(self, k):
        def inordert_arr(current, arr = []):
            if not current:
                return
            
            inordert_arr(current.left, arr)
            arr.append(current.value)
            inordert_arr(current.right, arr)
            return arr
        in_order = inordert_arr(self.root)
        return inordert_arr(self.root)[k-1] if len(in_order) >= k else None
    
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
        
        parent = ansessors.pop()

        if parent.right and parent.right.value == target.value:
            child = target
            while len(ansessors) and parent.right and parent.right.value == child.value:
                child  = parent
                parent = None if not ansessors else ansessors.pop()

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


        
