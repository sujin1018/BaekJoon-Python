def fib(n):
    global cnt1
    if n==1 or n==2:
        return 1
    cnt1+=1
    return fib(n-1)+fib(n-2)
def fibonacci(n):
    global cnt2
    dp=[1]*(n+1)
    for i in range(3,n+1):
        cnt2+=1
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
cnt1,cnt2=1,0
fib(n)
fibonacci(n)
print(cnt1,cnt2)