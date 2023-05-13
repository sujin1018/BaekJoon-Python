import sys
input=sys.stdin.readline
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
n=int(input())
t=[int(input()) for _ in range(n)]
s=[]
for i in range(1,n):
    s.append(t[i]-t[i-1])
res=s[0]
for i in range(1,len(s)):
    res=gcd(s[i],res)
cnt=0
for i in s:
    cnt+=i//res-1
print(cnt)