import sys, heapq
input=sys.stdin.readline
n=int(input())
a=[]
for _ in range(n):
    x=int(input())
    if x!=0:
        heapq.heappush(a,x)
    else:
        if not a:
            print(0)
        else:
            print(heapq.heappop(a))