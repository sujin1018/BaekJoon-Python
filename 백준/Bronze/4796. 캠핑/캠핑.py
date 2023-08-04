import sys
input=sys.stdin.readline
i=1
while True:
    l,p,v=map(int,input().split())
    if l==0 and p==0 and v==0:
        break
    res=l*(v//p)
    a=v%p
    if a>l:
        a=l
    print(f"Case {i}: {res+a}")
    i+=1