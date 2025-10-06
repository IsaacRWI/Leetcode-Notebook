from collections import deque
list1 = list([1,2,23,4,6])
q = deque(list1)
for i in range(len(q)):
    print(q[i])