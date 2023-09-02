import sys, heapq
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
q=[]
a.sort()
heapq.heappush(q, a[0][1])
for i in range(1,n):
    if q[0]>a[i][0]:
        heapq.heappush(q, a[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q,a[i][1])
print(len(q))