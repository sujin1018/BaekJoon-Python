from collections import deque
n=int(input())
a=[i for i in range(1,n+1)]
a=deque(a)
while len(a)>1:
    a.popleft()
    a.append(a.popleft())
print(a.pop())