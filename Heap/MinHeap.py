import math
class MinHeap:
    heap = []
    size = 0

    def __init__(self, lst=None):
        if lst:
            self.heap = lst.copy()
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
        return (node_index-1) // 2 if node_index > 0 else -1
    
    def _left_child_index(self, node_index):
        if node_index >= self.size//2 :
            return -1 
        pos = 2*node_index+1
        return pos if pos < self.size else -1 
    
    def _right_child_index(self, node_index):
        if node_index >= math.floor(self.size/2) :
            return -1 
        pos = 2*node_index+2
        return pos if pos < self.size else -1 

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
        
        parent = self.heap[index]
        if parent > self.heap[child_index]:
            self.heap[index], self.heap[child_index] = self.heap[child_index], parent
            return self._heapify_down(child_index)
        
    def _is_heap(self):
        # complete
        # the parent is smalle than the two child
        def is_smallest(pos):
            if pos == -1:
                return True
            
            right_pos = self._right_child_index(pos)
            left_pos  = self._left_child_index(pos)

            if right_pos != -1 and self.heap[pos] > self.heap[right_pos]:
                return False
            if left_pos != -1 and self.heap[pos] > self.heap[right_pos]:
                return False
            
            return is_smallest(right_pos) and is_smallest(left_pos)
        
        return is_smallest(0)


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
        self.size -= 1
        top = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self._heapify_down(0)
        self.heap[self.size] = top
        return top 
    
    def find_smaller_values(self, value):
        assert not self.is_empity()
        values = []
        
        def process(pos):
            
            if pos == -1 or pos >= self.size or self.heap[pos] >= value:
                return

            values.append(self.heap[pos])
            process(self._left_child_index(pos)) 
            process(self._right_child_index(pos))
         
        process(0)
        return values
    def heap_sort(self):
        for i in range(self.size):
            self.pop()
        self.heap.reverse()
        return True
        

        
        


        

min_heap = MinHeap([10,3,5,88,1,100])

# print(min_heap.find_smaller_values(10))
