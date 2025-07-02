# pos => Position
# val => value
import math
class MaxHeap:

    heap = []
    size = 0


    def __init__(self, lst=[]):
        if lst:
            self.heap = lst
            self.size = len(lst)
            for pos in range(self.size//2, -1, -1):
                self._heapify_down(pos)
    # protected
    def _parent_pos(self, index):
        assert 0 <= index < self.size
        return math.ceil(index/2)-1 if index else -1 
    
    def _left_child_pos(self, index):
        assert 0 <= index < self.size
        return index*2+1 if index < self.size // 2 else -1
    
    def _right_child_pos(self, index):
        assert 0 <= index < self.size
        pos = index*2+2
        return pos if index < self.size // 2 and pos < self.size else -1
    
    def _fix_last(self):
        self._heapify_down(self.size-1)

    def _heapify_down(self, pos): # start from child
        parent_pos = self._parent_pos(pos)
        if parent_pos == -1:
            return
        child = self.heap[pos]
        if self.heap[parent_pos] > child:
            return
        self.heap[pos], self.heap[parent_pos]  = self.heap[parent_pos], child
        return self._heapify_down(parent_pos) 

    def _heapify_up(self, pos): #start from the parent
        child_pos = self._left_child_pos(pos)
        right_child_pos = self._right_child_pos(pos)

        if child_pos == -1:
            return

        if right_child_pos != -1 and self.heap[child_pos] < self.heap[right_child_pos]:
            child_pos = right_child_pos
        
        child = self.heap[child_pos]

        if child < self.heap[pos]:
            return
        
        
        self.heap[child_pos], self.heap[pos]  = self.heap[pos], child
        return self._heapify_up(child_pos)


    # Public
    def is_empity(self):
        return False if self.size else True
    
    def top(self):
        return self.heap[0]

    def push(self, val):
        self.size += 1
        self.heap.append(val)
        self._fix_last()


    def pop(self):
        assert not self.is_empity()
        top = self.top()
        if self.size == 1:
            self.heap = []
            return top
        self.heap[0] = self.heap[self.size-1]

        # self.size -= 1

        self._heapify_up(0) 

        self.size -= 1
        self.heap[self.size] = None
        self.heap.remove(None)
        return top


max_heap = MaxHeap([15,5,100,20])
# max_heap.push(15)
# max_heap.push(5)
# max_heap.push(100)
# max_heap.push(20)

print(max_heap.heap)

for i in range(max_heap.size):
    print(max_heap.pop(), end=' ')

print('\n--')

print(max_heap.heap)