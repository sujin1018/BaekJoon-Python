n=int(input())
a=input()
res=0
for i in range(n):
    res+=(ord(a[i])-96)*(31**i)
print(res)    