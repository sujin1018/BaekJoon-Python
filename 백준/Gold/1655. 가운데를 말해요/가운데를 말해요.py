import sys,heapq
input=sys.stdin.readline
n=int(input())
s1,s2=[],[]
for _ in range(n):
    a=int(input())
    if len(s1)==len(s2):
        heapq.heappush(s1,a*(-1))
    else:
        heapq.heappush(s2,a)
    if len(s1)>=1 and len(s2)>=1 and s1[0]*(-1)>s2[0]:
        max_v=heapq.heappop(s1)*(-1)
        min_v=heapq.heappop(s2)
        heapq.heappush(s1,min_v*(-1))
        heapq.heappush(s2,max_v)
    print(s1[0]*(-1))