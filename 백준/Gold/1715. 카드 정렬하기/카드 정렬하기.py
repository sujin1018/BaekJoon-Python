import sys,heapq
input=sys.stdin.readline
n=int(input())
a=[]
for _ in range(n):
    heapq.heappush(a,int(input()))
res=0
while len(a)>1:
    n1=heapq.heappop(a)
    n2=heapq.heappop(a)
    res+=(n1+n2)
    heapq.heappush(a,n1+n2)
print(res)