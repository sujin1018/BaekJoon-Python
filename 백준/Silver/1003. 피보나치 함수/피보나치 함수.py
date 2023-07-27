import sys
input=sys.stdin.readline
zero=[1,0,1]
one=[0,1,1]
def f(n):
    l=len(zero)
    if n>=l:
        for i in range(l,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])
t=int(input())
for _ in range(t):
    f(int(input()))