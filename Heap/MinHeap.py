import math
class MinHeap:
    heap = []
    size = 0

    def __init__(self, lst=None):
        if lst:
            self.heap = lst
            self.size = len(lst)
            self._heapify()

    def _heapify(self):
        assert not self.is_empity()
        for i in range(self.size//2 -1, -1, -1):
            self._heapify_down(i)
        

    def _size(self):
        return self.size
    
    def _top(self):
        assert self._size()
        return self.heap[0]
    
    def _parent_index(self, node_index):
        return math.floor((node_index-1) / 2) if node_index > 0 else -1
    
    def _left_child_index(self, node_index):
        if node_index >= math.floor(self.size/2) :
            return -1 
        return 2*node_index+1 if node_index < self.size else -1 
    
    def _right_child_index(self, node_index):
        if node_index >= math.floor(self.size/2) :
            return -1 
        return 2*node_index+2 if node_index < self.size else -1 

    def _fix(self, index):
        assert index >= 0 and index <= len(self.heap)
        if index < 1 or len(self.heap) <= 1 :
            return
        
        parent_index = self._parent_index(index)
        node   = self.heap[index]
        parent = self.heap[parent_index]

        if parent <= node:
            return
        
        self.heap[parent_index], self.heap[index]  = node, parent

        self._fix(parent_index)

    def _heapify_down(self, index):
        child_index = self._left_child_index(index)
        right_child_index = self._right_child_index(index)

        if child_index == -1:
            return 

        if right_child_index != -1 and self.heap[child_index] > self.heap[right_child_index]:
            child_index = right_child_index
        
        if self.heap[index] > self.heap[child_index]:
             parent = self.heap[index]
             self.heap[index], self.heap[child_index] = self.heap[child_index], parent
             return self._heapify_down(child_index)

    ## --- public ---  

    def is_empity(self):
        return False if self.size else True 

    def push(self, value):
        self.heap.append(value)
        self.size += 1
        self._fix(len(self.heap)-1)
        return True
    
    def pop(self): # remove top element
        assert not self.is_empity()

        if self.size == 1:
            top    =  self._top()
            self.heap = []
            return top 

        top = self.heap[0]

        self.heap[0] = self.heap[self.size-1]
        
        self.size -= 1
        self._heapify_down(0)
        self.heap[self.size] = None
        return top 
        

min_heap = MinHeap([10,3,5,1,100])
min_heap.pop()
print(min_heap.heap)
