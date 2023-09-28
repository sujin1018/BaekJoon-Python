import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
ad,mi,mu,di=map(int,input().split())
max_num=-1e9
min_num=1e9
def dfs(idx,total,ad,mi,mu,di):
    global max_num, min_num
    if idx==n:
        max_num=max(total,max_num)
        min_num=min(total,min_num)
        return
    if ad:
        dfs(idx+1,total+a[idx],ad-1,mi,mu,di)
    if mi:
        dfs(idx+1,total-a[idx],ad,mi-1,mu,di)
    if mu:
        dfs(idx+1,total*a[idx],ad,mi,mu-1,di)
    if di:
        dfs(idx+1,int(total/a[idx]),ad,mi,mu,di-1)
dfs(1,a[0],ad,mi,mu,di)
print(max_num)
print(min_num)