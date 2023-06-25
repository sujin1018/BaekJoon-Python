import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
r=a[-1]
cnt=1
for i in a[::-1]:
    if i>r:
        r=i
        cnt+=1
print(cnt)