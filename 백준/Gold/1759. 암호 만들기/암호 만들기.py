li=['a','e','i','o','u']
l,c=map(int,input().split())
s=sorted(input().split())
res=[]
def back(cnt, idx):
    if cnt==l:
        a,b=0,0
        for i in range(l):
            if res[i] in li:
                a+=1
            else:
                b+=1
        if a>=1 and b>=2:
            print("".join(res))
        return
    for i in range(idx,c):
        res.append(s[i])
        back(cnt+1,i+1)
        res.pop()
back(0,0)