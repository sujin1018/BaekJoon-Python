import sys
input=sys.stdin.readline
cnt=0
while True:
    o,w=map(int,input().split())
    die=False
    if o==0 and w==0:
        break
    while True:
        a,b=input().rstrip().split()
        if a=='#' and b=='0':
            break
        if not die:
            if a=='F':
                w+=int(b)
            elif a=='E':
                w-=int(b)
        if w<=0:
            die=True
    cnt+=1
    if w<=0:
        print("%d RIP" %cnt)
    elif (o/2)<w<(o*2):
        print("%d :-)" %cnt)
    else:
        print("%d :-(" %cnt)