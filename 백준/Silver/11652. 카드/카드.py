import sys
input=sys.stdin.readline
n=int(input())
d={}
for i in range(n):
    a=int(input())
    if a in d:
        d[a] +=1
    else:
        d[a] = 1
res = sorted(d.items(), key=lambda x:(-x[1],x[0]))
print(res[0][0])