import sys
input=sys.stdin.readline
n=input().rstrip()
s=[]
for i in range(1,len(n)-1):
    for j in range(i+1,len(n)):
        a,b,c=n[:i],n[i:j],n[j:]
        s.append(a[::-1]+b[::-1]+c[::-1])
print(min(s))