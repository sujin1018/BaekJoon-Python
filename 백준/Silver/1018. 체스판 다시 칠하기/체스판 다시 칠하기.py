import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[input().strip() for _ in range(n)]
res=[]
for x in range(n-7):
    for y in range(m-7):
        w=0
        b=0
        for i in range(x,x+8):
            for j in range(y,y+8):
                if (i+j)%2==0:
                    if a[i][j]!='W':
                        w+=1
                    if a[i][j]!='B':
                        b+=1
                else:
                    if a[i][j]!='W':
                        b+=1
                    if a[i][j]!='B':
                        w+=1
        res.append(min(w,b))
print(min(res))