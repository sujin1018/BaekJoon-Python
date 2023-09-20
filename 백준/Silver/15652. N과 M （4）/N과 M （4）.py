n,m=map(int,input().split())
a=[]
def n_m(x):
    if len(a)==m:
        print(' '.join(map(str,a)))
        return
    for i in range(x,n+1):
        a.append(i)
        n_m(i)
        a.pop()
n_m(1)