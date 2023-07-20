from collections import deque
n=int(input())
s=deque(enumerate(map(int,input().split())))
for _ in range(n):
    p=s.popleft()
    print(p[0]+1,end=' ')
    if p[1]>0:
        s.rotate(-(p[1]-1))
    else:
        s.rotate(-p[1])