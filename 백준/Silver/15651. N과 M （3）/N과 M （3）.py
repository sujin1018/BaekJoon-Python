n,m=map(int,input().split())
a=[]
def n_m():
    if len(a)==m:
        print(' '.join(map(str,a)))
        return
    for i in range(1,n+1):
        a.append(i)
        n_m()
        a.pop()
n_m()