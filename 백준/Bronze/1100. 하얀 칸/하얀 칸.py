import sys
input=sys.stdin.readline
a=[list(input().rstrip()) for _ in range(8)]
cnt=0
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            if a[i][j]=='F':
                cnt+=1
print(cnt)