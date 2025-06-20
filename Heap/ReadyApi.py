import heapq


lst = [1, 15, 16, 17, 21, 5, 77]

heapq.heapify(lst)

print(lst)

for val in range(len(lst)):
    print(heapq.heappop(lst), end=' ')

print()
print('-'*6)

lst = [1, 15, 16, 17, 21, 5, 77]


print(heapq.nlargest(3, lst))
print(heapq.nsmallest(3, lst))

print()
print('-'*6)


lst = [1, 15, 16, 17, 21, 5, 77]
min_heap = [11]

for val in lst:
    heapq.heappush(min_heap, val)

print(min_heap)