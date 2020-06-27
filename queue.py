from collections import deque#using predefined module
q=deque()
q.append('a')#adding elements
q.append('b')
q.append('c')
print(q,'\n')#printing the queue
a=q.popleft()#deleting from left side
print('Popped element is',a)
b=q.popleft()
print('Popped element is',b)
c=q.popleft()
print('Popped element is',c)
