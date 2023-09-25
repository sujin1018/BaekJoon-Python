import sys
input=sys.stdin.readline
n=int(input())
s=[0]+[int(input()) for _ in range(n)]
dp=[0]*301
if n<=2:
    print(sum(s))
else:
    dp[1]=s[1]
    dp[2]=s[1]+s[2]
    dp[3]=max(s[1]+s[3],s[2]+s[3])
    for i in range(4,n+1):
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[n])