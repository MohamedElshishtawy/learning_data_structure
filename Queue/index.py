class Queue:
    
    memory = []
    head = 0
    tail = -1
    capacity = 5

    def enqueue(self, value):
        if len(self.memory) < self.capacity:
            self.memory.append(value)
            self.tail += 1
        else:
            if self.tail+1 == self.capacity and self.memory[0] == -1:
                self.tail = 0
                self.memory[0] = value
            else:
                if self.memory[self.tail+1] == -1:
                    self.tail += 1
                    self.memory[self.tail] = value
                else:
                    return False
            


    def dequeue(self):
        self.memory[self.head] = -1
        self.head %= self.head +1

    def show(self):
        print(self.memory)

