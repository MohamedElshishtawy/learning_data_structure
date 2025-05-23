class Node:
    left = None
    right = None
    value = 0

    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    def _is_leaf(self):
        return not self.left and not self.right


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
                    raise TypeError(f"Left not correct for {value}")
                prev = prev.left
            else:
                if not prev.right:
                    prev.right = Node(None, None, value)
                elif prev.right.value != value:
                    raise TypeError(f"Right not correct for {value}")
                prev = prev.right

    def pree_order_arr(self):
        def iterate(current, result):
            if not current:
                return
            result.append(current.value)
            iterate(current.left, result)
            iterate(current.right, result)
            return result

        return iterate(self.root, [])

    def show(self):
        def iterate(current):
            if not current:
                return
            iterate(current.left)
            print(current.value, end=' ')
            iterate(current.right)

        iterate(self.root)
        print()

    def find(self, val):
        current = self.root
        while current:
            if current.value == val:
                return self.pree_order_arr(current)
            elif current.value < val:
                current = current.right
            else:
                current = current.left

    def _find_node(self, val):
        current = self.root
        while current:
            if current.value == val:
                return current
            elif current.value < val:
                current = current.right
            else:
                current = current.left
        return []

    def valid_BST(self):
        def is_valid(current, mn=float('-inf'), mx=float('inf')):
            if not current:
                return True
            if not (mn < current.value < mx):
                return False
            return is_valid(current.left, mn, current.value) and is_valid(current.right, current.value, mx)

        return is_valid(self.root)

    def min(self, target=None):
        def iterate(current):
            if not current:
                return
            if not current.left:
                return current
            return iterate(current.left)

        return iterate(self.root) if not target else iterate(target)

    def kth(self, k):
        def inordert_arr(current, arr=[]):
            if not current:
                return
            inordert_arr(current.left, arr)
            arr.append(current.value)
            inordert_arr(current.right, arr)
            return arr

        in_order = inordert_arr(self.root)
        return in_order[k - 1] if len(in_order) >= k else None

    def _find_ansessors_chain(self, target):
        def iterate(current):
            if not current:
                return False
            self.ansessors.append(current)
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
        ansessors = self._find_ansessors_chain(target)
        target = ansessors.pop()
        if target.right:
            return self.min(target.right)
        parent = ansessors.pop() if ansessors else None
        if parent and parent.left and parent.left.value == target.value:
            return parent
        while ansessors:
            child = parent
            parent = ansessors.pop()
            if parent.left == child:
                return parent
        return None

    def delete(self, val):
        def iterate(current, val):
            if not current:
                return current
            if current.value > val:
                current.left = iterate(current.left, val)
            elif current.value < val:
                current.right = iterate(current.right, val)
            else:
                if current._is_leaf():
                    return None
                if current.left and not current.right or not current.left and current.right:
                    return current.left if current.left else current.right
                else:
                    parent, child = current, current.right
                    while child.left:
                        parent, child = child, child.left
                    if parent.left == child:
                        parent.left = child.right
                    else:
                        parent.right = child.right
                    current.value = child.value
                    return current

        self.root = iterate(self.root, val)


# --------------- Test Cases ----------------

print("Test 1: Root only")
t1 = Tree(50)
t1.show()  # Expected: 50

print("Test 2: Add left and right")
t2 = Tree(10)
t2.add([5], ['L'])
t2.add([15], ['R'])
t2.show()  # Expected: 5 10 15

print("Test 3: Conflict")
t3 = Tree(10)
t3.add([5], ['L'])
try:
    t3.add([6], ['L'])  # Conflict
except TypeError as e:
    print("Caught:", e)  # Expected error

print("Test 4: Pre-order")
t4 = Tree(10)
t4.add([5], ['L'])
t4.add([15], ['R'])
print("Pre-order:", t4.pree_order_arr())  # Expected: [10, 5, 15]

print("Test 5: kth element")
t5 = Tree(20)
t5.add([10, 5], ['L', 'L'])
t5.add([10, 15], ['L', 'R'])
t5.add([30, 25], ['R', 'L'])
print("3rd smallest:", t5.kth(3))  # Expected: 15

print("Test 6: Valid BST")
t6 = Tree(10)
t6.add([5], ['L'])
t6.add([15], ['R'])
print("Is BST:", t6.valid_BST())  # True

print("Test 7: Invalid BST (tamper)")
t7 = Tree(10)
t7.add([5], ['L'])
t7.add([15], ['R'])
t7.root.left.value = 20
print("Is BST:", t7.valid_BST())  # False

print("Test 8: Delete leaf")
t8 = Tree(10)
t8.add([5], ['L'])
t8.add([15], ['R'])
t8.delete(5)
t8.show()  # Expected: 10 15

print("Test 9: Delete node with one child")
t9 = Tree(10)
t9.add([5, 3], ['L', 'L'])
t9.delete(5)
t9.show()  # Expected: 3 10

print("Test 10: Delete node with two children")
t10 = Tree(20)
t10.add([10, 5], ['L', 'L'])
t10.add([10, 15], ['L', 'R'])
t10.add([30, 25], ['R', 'L'])
t10.add([30, 35], ['R', 'R'])
t10.delete(10)
t10.show()  # Expected: 5 15 20 25 30 35
