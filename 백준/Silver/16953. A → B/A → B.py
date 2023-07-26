from collections import deque
a,b=map(int,input().split())
q=deque([(a,1)])
while q:
    i,cnt=q.popleft()
    if i==b:
        print(cnt)
        break
    if i*10+1<=b:
        q.append((i*10+1,cnt+1))
    if i*2<=b:
        q.append((i*2,cnt+1))
else:
    print(-1)  