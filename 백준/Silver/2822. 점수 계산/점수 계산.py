import sys
input=sys.stdin.readline
a=[int(input()) for _ in range(8)]
res=sorted(a,reverse=True)
b=[a.index(i)+1 for i in res[:5]]
b.sort()
print(sum(res[:5]))
print(*b)