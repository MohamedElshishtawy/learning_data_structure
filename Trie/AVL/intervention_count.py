from AVL import AVL

def invertion_count(values = []):
    count = 0
    
    avl = AVL(values[0])

    for val in values[1:]:
        count += avl.count_greate(val)
        avl.insert(val)

    return count

print(invertion_count([10, 5, 8, 2, 12, 6]))