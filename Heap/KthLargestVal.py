class KthLargestVal:
    arr = []
    k   = 0
    size = 0
    
    def __init__(self, arr, k):
        self.arr = arr
        self.k   = k
        self.size = len(arr)

    def process(self):
        result = []
        for inx, val in enumerate(self.arr):
            smallest = val
            for i in range(inx, inx-self.k, -1):
                if i >= self.size or i < 0 :
                    break
                com_val = self.arr[i]
                if com_val < smallest:
                    smallest = com_val
            result.append(smallest)
        return result 

keyboardInterrupt = KthLargestVal([2,17,22,10,8,37,14,19,7,6,5,12,25,30], 4)               
print(keyboardInterrupt.process())