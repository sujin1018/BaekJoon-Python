import sys,heapq
input=sys.stdin.readline
n=int(input())
q=[]
for _ in range(n):
    arr=list(map(int,input().split()))
    if not q:
        for i in arr:
            heapq.heappush(q,i)
    else:
        for i in arr:
            if q[0] < i:
                heapq.heappop(q)
                heapq.heappush(q,i)
print(q[0])