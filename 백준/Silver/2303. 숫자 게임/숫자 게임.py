import sys
input=sys.stdin.readline
n=int(input())
s=[]
for _ in range(n):
    a=list(map(int,input().split()))
    res=0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                o=(a[i]+a[j]+a[k])%10
                if o>=res:
                    res=o
    s.append(res)
for i in range(n-1,-1,-1):
    if s[i]==max(s):
        print(i+1)
        break