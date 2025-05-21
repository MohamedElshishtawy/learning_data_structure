
class Stack:
    
    memory = []
    lenght = 0

    def __init__(self, values=None):
        if values :
            for value in values:
                self.push(value)        

    def push(self, value):
        self.memory.append(value)
        self.lenght += 1
    
    def pop(self):
        if self.lenght > 0:
            self.lenght -= 1
            return self.memory.pop()
        return -1
        
    
    def top(self):
        return self.memory[-1]
    
    def show(self):
        print('[', end=' ')
        self.memory.reverse()
        for value in self.memory:
            print(value, end=' ')

        print(']', end=' ')
    
# sack = Stack()
# sack.push(12)
# sack.push(13)
# sack.push(14)
# sack.push(15)
# sack.pop()
# sack.show()

num = 1234000


def reverse(number):
    num = str(number)
    stk = Stack()
    result = ''
    for i in num:
        stk.push(i)
    
    for i in range(stk.lenght):
        result += stk.pop()

    return int(result)


def valid_paransces(value):
    data = {')': '(','}': '{',']': '['}
    stk = Stack()

    for val in value:
        if val in data.values():
            stk.push(val)
        elif val in data.keys():
            if data[val] != stk.pop():
                return False
        else:
            return False
        
    if stk.lenght > 0:
        return False
    
    return True
# def do_colligue(value, direction):
#      if direction.top() > 0:
#         # Colliigeen
#         if direction.top() < 0:
#             direction.push(value)
#         else:
#             if direction.top() > value:
#                 return
#             else:
#                 direction.pop()
#                 do_colligue(value, direction)

# def colliage(arr):
#     direction = Stack()
#     for value in arr:
#         if value > 0:
#             direction.push(value)
#         else:
#             do_colligue(value, direction)
#     direction.show()


       
def colliage(astroids):
    result = []
    for ast in astroids:
        if ast > 0:
            result.append(ast)
            continue
        
        while result and result[-1] >= 0 and ast < 0:
            if -ast < result[-1]:
                break
            elif -ast == result[-1]:
                result.pop()
                break
            else:
                result.pop()
        else:
            result.append(ast)
    print(result) 


# colliage([10,2,-5, -10, 0 , 10])

def calc_parances(parances):
    stk = []
    result = 0
    for char in parances:
        if char == '(':
            stk.append(0)
        else:
            if stk and stk[-1] == 0:
                stk.pop()
                result += 1
                if stk:
                    stk[-1] += 1
            else:
                result = 2*stk[-1]
                stk.pop()
                if stk:
                    stk[-1] += result
    print(stk)
    return result

print(calc_parances('()((())())'))
