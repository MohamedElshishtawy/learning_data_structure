
class Node:
    next = None
    value = 0

    def __init__(self, val) -> None:
        self.value = val


class Linked_list:

    start = end = None
    size  = 0

    def __init__(self, values=None) -> None:
        if values  :
            for value in values:
                self.insert_end(value)

    def show(self):
        if self.size <= 0:
            return -1
        node = self.start
        print('[', end='')
        while node:
            print(node.value, end='')
            node = node.next
            if node != None : 
                print(', ', end='')
        print(']') 
    def __iter__(self):
        node = self.start
        while node:
            yield node.value
            node = node.next  

    def _debug(self):
        messages = []
        if (self.size):
            if self.start:
                node = self.start
                prev = None
                nodes_count = 0
                while node:
                    prev = node
                    node = node.next
                    nodes_count += 1
                if nodes_count != self.size:
                    messages.append('Error: there is a wrong in size or in next relations') # Problem I can't know
                if prev != self.end:
                    messages.append('Error the Last elemnt no the end')

            else:
                messages.append('Error: Start not have value')
        else:
            messages.append('size is zero')

    def insert_end(self, value):
        new_item = Node(value)
        if self.end:
            self.end.next = new_item
        else:
            self.start = new_item
        self.end = new_item
        self.size += 1
    def eq(self, index):
        if 0 > index >= self.size:
            return None
        node = self.start
        for i in range(self.size):
            if i == index:
                return node.value
            node = node.next
    def search(self, value):
        node = self.start
        index = 0
        while node:
            if node.value == value:
                return index
            index += 1
            node = node.next
        return -1

    def delete(self, val):
        node = self.start
        before = None
        while node:
            if node.value == val:
                if before != None:
                    before.next = node.next
                    del node
                else:
                    self.start = node.next
                    del node
                return True
            before = node
            node = node.next
        return -1

    def pair_swap(self):
        node = self.start
        while node  and node.next:
            temp = node.value
            node.value, node.next.value = node.next.value, temp
            node = node.next.next
        return True


    def reverse(self):
        """
        It should be O(1)
        """
        if self.size <= 0:
            return -1
        self.end = self.start

        prev = self.start
        self.start = self.start.next
        while self.start:
            # Temp
            next = self.start.next
            # Change channel
            self.start.next = prev
            # Reorder vars
            prev = self.start
            self.start = next
        if prev:
            self.start = prev
            self.end.next = None


    
    def improve(self, value):
        before_before = None
        before_node = None
        node = self.start

        while node:
            if node.value == value:
                if before_before :
                    before_before.next = node
                    before_node.next = node.next
                    node.next = before_node
                    # if it is the last elemnt has beeb changed
                    if not node.next:
                        self.end = node
                elif before_node:
                    before_node.next = node.next
                    node.next = before_node
                    self.start = node
                    

                    return True        
            if before_node :
                before_before = before_node
            before_node = node
            node = node.next

        return False

    def middle(self):
        slow = self.start
        fast = self.start
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    

    
        
