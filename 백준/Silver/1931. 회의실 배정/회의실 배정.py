import sys
input=sys.stdin.readline
n=int(input())
time=[[0]*2 for _ in range(n)]
for i in range(n):
    a,b=map(int,input().split())
    time[i][0]=a
    time[i][1]=b
time.sort(key=lambda x:(x[1],x[0]))
last,cnt=0,0
for i,j in time:
    if i>=last:
        cnt+=1
        last=j
print(cnt)