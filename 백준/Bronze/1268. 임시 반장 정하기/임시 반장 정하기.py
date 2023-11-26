import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=[[0 for _ in range(n)] for _ in range(n)]
for k in range(5):
    for i in range(n):
        for j in range(i+1,n):
            if a[i][k]==a[j][k]:
                res[i][j]=1
                res[j][i]=1
cnt=[]
for i in res:
    cnt.append(i.count(1))
print(cnt.index(max(cnt))+1)